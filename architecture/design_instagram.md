# Design Instagram System Design Answer

## Requirements

Upload images from a mobile client
Allow users to follow other users
Generate a feed of images and display that to users when they visit the app
Think about API to request that feed and ensure it is generated reliably
Think about scalability to support 10m users

Questions:
Do we want to support other clients?
What are some constraints?
Any networking concerns?
Any storage concerns?
Any cost concerns?
What is the expected latency of getting images?
How often should content refresh?
Should the feed only be people you follow or also explore feature?

## Scaling

With 10m active monthly users, let's imagine each is uploading 2 photos per month.
Let's say each photo is around 5mb (caption, photo metadata). Let's ignore comments for now
so 10m * 2 * 5mb = 100m mb, which is 100tb per month, or 1.2pb per year
This informs the load of traffic we can expect. We will have to think about ways to store
that data and how to do it in ways that are reliable and efficient.

## Data Model

3 different data types: users, photos, user following relationship
Sketch out these 3 tables and talk about the kinds of DB you would use for this kind of data
This is a fundamental relational data problem, with following and photos from users, etc.
Consider whether data is relational and whether you would benefit from doing relational queries.
We will use SQL instead of NoSQL.

Users
user_id pk int auto_inc
name str
email str
location str
join_date datetime

Photos
photo_id pk int auto_inc
user_id fk
caption str
location str
path str (reference to distributed filesystem that actually holds the file)

Followers
base_user_id fk int
followed_user_id fk int

## Overall System

We have a DB that is our SQL metadata DB. Store the reference paths to the actual images in the Photos table of the metadata DB.

We have a cloud distributed storage service for storing the files S3/GCS (will store and replicate our data in a reliable way)

App Service Layer (responsible for CRUD). Responds to requests from clients whether mobile/web/etc and will handle them and then perform operations on the DB and will get data from the DB and return it to the user. You usually start with a monolith web app and as traffic scales up, you can break it out into microservices that can scale independently and perform specific operations to optimize server usage.

There will be many more ppl viewing their feed than there will be uploading. We need to be able to do both of those operations efficiently and support different access patterns (peak times of day). All sorts of usage patterns will mean we will want to scale up/down at different times. 

This is a read heavy system, so we will want replicas of the DB so that we can do this quickly without slowing down our ability to upload images. This will help us scale and DB connections are often a major bottleneck of a system.

So build an app server that has a split of read services and writing services. Might implement caching in between the DB and the app server, like Redis, so that we can return frequently accessed data much faster than making a request to the DB every single time. Read from the Cache when able. Write service will write to the DB and update the cache in the process. We want to use write back caching policy where when an update happens on our DB, we want to update the Cache at the same time to keep it consistent with the source of truth in the main DB. So now we have 2 different services, one is responsible for fetching images and returning data to the user and the other is responsible for performing the upload process, which sends data into the Metadata DB, uploading the image from the client to the file storage system, and updating the Cache.

We also need a load balancer. As any system scales, it becomes impotant that system can handle the load and volume of number of users that are attempting to use it, otherwise you will drop requests or take a long time to respond to users. One of the common patterns to fix this is to scale horizontally. So instead of having one app server for reading and one for writing, we would have many, located in many different zones so that they could field close by requests. We would serve requests to the servers in a load balanced way so that each one is utilized equally with the others as much as possible so that no server is too overloaded or overworked. You can have separate load balancers, one for load balancing and one for routing.

Mobile client will be sending a request to the Load Balancer and it will be processed from there. Sends all the types of requests. Starting from the client, they will call our API, which will have different routes for the different requests for features we support (like loading pages, uploading images, etc). Request will hit Load Balancer, it will get the request, figure out where to send it, will send it to that service. In a read case, it will do the business logic to identify which image the user is looking for, check if they have access to it, will look to the cache first to see if it is in there, if so, it will return the image data and user metadata it needs, the response comes all the way back through to the mobile client, that info will include the path to the image that needs to be loaded. That loading request will be fired off separately and will be loaded in a separate request from the distributed filesystem. Sitting between here might be a CDN or Distribution Network that would make these requests faster by having access points that are closer to make the last mile request latency much faster. In the upload case, something similar would happen where a connection to the server is opened, it would begin to upload all the meta data related to the user and the photo that is being uploaded. It would handle receiving the image and passing it on into the object storage. That process would also cause the cache to be updated, so that the cache is up to date. Feed generation is a process that could be stored in a cache and could be managed by a separate service. Feed generation service would access cache and DB and would be operating on a schedule, perhaps generating a new feed for every user on an hourly basis and would talk to DB to understand what was new and would generate these things ahead of time and store them in the cache and allow the app server that is responsible for getting the feed to just read the cached results.

A GOOD ADDITION WOULD BE ADDING A MESSAGING QUEUE FOR UPLOADING THE IMAGES. This will help handle large file sizes and slow processing times with a pub/sub pull model where workers can pull another image off the queue to upload when they are ready.

Mobile Client (or any client)--------------------------------------------------------------|
    |                                           ,--Feed Generation Service                 |
    V                                           V             |                            |
Load Balancer ---> App Server (read) ---> Cache (Redis) <--,  V                            V
    `-----------> App Server (write) --------------> Metadata DB ----filepath---> Object Storage (GCS)
                        `------upload image-----------------------------------------------^


- `App Engine` (platform as a service, fully managed, auto scaling, serverless, host web apps at scale, can scale to 0 if no requests) or `Compute Engine` (infra as a a service, costs less, more flexibility, harder to use) for Servers
- `NGINX` for Load Balancing
- `Pub/Sub` for Queue (push or pull, replaces Kafka)
- `Dataflow` for Pipelines
- `Dataproc` for Spark
- `BigTable` (time series or transactions) or `Firestore` for NoSQL
- `Cloud SQL` MySQL for OLTP
- `BigQuery` for OLAP
- `GCS` for storage
- `Datalab` for Jupyter Notebooks
- `Data Studio` for BI 
- `Cloud Composer` or `Airflow` for Orchestration

Issues to Consider:
- `Latency`: Network latency is the amount of time it takes for a data packet to go from one place to another. Use of a CDN (content delivery network) is a major step towards reducing latency. A CDN caches static content and serves it to users. (The Cloudflare CDN makes it possible to cache dynamic content as well with Cloudflare Workers.) CDN servers are distributed in multiple locations so that content is stored closer to end users and does not need to travel as far to reach them. This means that loading a webpage will take less time, improving website speed and performance. A webpage can be configured to load the above-the-fold area of a page first so that users can begin interacting with the page even before it finishes loading (above the fold refers to what appears in a browser window before the user scrolls down). Webpages can also load assets only as they are needed, using a technique known as lazy loading. These approaches do not actually improve network latency, but they do improve the user's perception of page speed. Sometimes, network "latency" (slow network performance) is caused by issues on the user's side, not the server side (slow internet or bad connection). Latency, bandwidth, and throughput are all interrelated, but they all measure different things. Bandwidth is the maximum amount of data that can pass through the network at any given time. Throughput is the average amount of data that actually passes through over a given period of time. Throughput is not necessarily equivalent to bandwidth, because it is affected by latency and other factors. Latency is a measurement of time, not of how much data is downloaded over time.
- `Eventual Consistency`: Eventual Consistency is a guarantee that when an update is made in a distributed database, that update will eventually be reflected in all nodes that store the data, resulting in the same response every time the data is queried. A key benefit of an eventually consistent database is that it supports the high availability model of NoSQL. Eventually consistent databases prioritize availability over strong consistency. Eventual consistency in microservices can support an always-available API that must be responsive, even if the query results may occasionally be missing the latest commit. A DBMS using the ACID model expects a unit of work to be atomic. It is all-or-nothing. While that unit of work is being done, the records or tables affected may be locked. Distributed databases with a BASE model give high availability. The records stay available, but once the transaction has completed across a majority of nodes, the transaction is deemed successful. Data replication across all nodes can take a little more time, but the data in all nodes will become consistent eventually. Once the transaction is deemed successful, queries for the data will consistently provide the updated data, even before data replication reaches the last few nodes. So, SQL is consistent, whereas NoSQL is eventually consistent.
- `Idempotence`: Running a data pipeline multiple times with the same input will always produce the same output. A common way to make your data pipeline idempotent is to use the delete-write pattern. As the name implies, the pipeline will first delete the existing data before writing new data. Be very careful to only delete data that the data pipeline will re-create. OVERWRITE is safer than delete, write and most libraries offer an overwrite option (Snowflake and Spark included). Idempotency prevents duplicates, removes stale data, saves on data storage cost.

ACID (SQL)
- `Atomicity`: if transaction fails at any point, the entire operation rolls back
- `Consistency`: the database remains structurally sound with every transaction
- `Isolation`: each transaction is independent of any other transaction
- `Durability`: all transaction results are permanently preserved

BASE (NoSQL)
- `Basic Availability`: data is available most of the time, even during a partial system failure.
- `Soft state`: replicas are not consistent all the time.
- `Eventual consistency`: data will become consistent at some point in time, with no guarantee when.

Values:
`innovative`, `collaborative`, `sincere`, `passionate`, `playful`

`The Band Manifesto`, `T Shaped Engineers`
