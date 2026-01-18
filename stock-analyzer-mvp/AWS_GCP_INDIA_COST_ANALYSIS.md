# AWS vs GCP India Region Cost Analysis

**Document Date**: January 18, 2026  
**Application**: Stock Analyzer MVP (Penny Stocks)  
**Target Region**: India (AWS Mumbai ap-south-1 / GCP Delhi region)  
**Deployment Model**: Containerized microservices

---

## Executive Summary

### Cost Comparison (Monthly)

| Service                 | AWS Mumbai   | GCP Delhi    | Winner |
| ----------------------- | ------------ | ------------ | ------ |
| **Baseline (Dev/Test)** | $120-150     | $140-180     | AWS    |
| **Production (Small)**  | $400-500     | $450-600     | AWS    |
| **Production (Scale)**  | $1,200-1,500 | $1,400-1,800 | AWS    |

**Recommendation**: **AWS is 15-20% cheaper** in India region, especially for containerized workloads.

---

## 🇮🇳 INDIA-FOCUSED COST ANALYSIS (IN RUPEES)

### Executive Summary - INR Pricing

**Exchange Rate Used**: 1 USD = ₹83 (as of Jan 2026)

| Service                | AWS Mumbai (₹)  | GCP Delhi (₹)    | Winner |
| ---------------------- | --------------- | ---------------- | ------ |
| **Dev/Test**           | ₹10,000-12,500  | ₹11,600-15,000   | AWS    |
| **Production (Small)** | ₹33,200-41,500  | ₹37,350-49,800   | AWS    |
| **Production (Scale)** | ₹99,600-124,500 | ₹116,200-149,400 | AWS    |

**Annual Savings (AWS vs GCP)**: ₹50,000-80,000+ for small-medium deployments

### India Stock Exchange Market Support

#### Supported Markets:

1. **NSE (National Stock Exchange)** ✅

   - Equities: 2,000+ listed companies
   - F&O: Futures & Options
   - Indices: NIFTY 50, NIFTY 100, etc.
   - Micro-cap stocks available

2. **BSE (Bombay Stock Exchange)** ✅

   - Equities: 5,000+ listed companies
   - SME Platform: Emerging companies
   - Penny stocks (< ₹50)

3. **MCX (Multi Commodity Exchange)** ✅
   - Commodities: Gold, Silver, Crude Oil
   - Agricultural futures

#### Data Provider Options (India):

| Provider             | Market       | API Cost/Month | Free Tier  | Best For        |
| -------------------- | ------------ | -------------- | ---------- | --------------- |
| **NSE (Direct)**     | NSE Equities | ₹50,000+       | None       | Institutional   |
| **BSE (Direct)**     | BSE Equities | ₹75,000+       | None       | Institutional   |
| **Upstox API**       | NSE/BSE      | ₹5,000/month   | ✅ 50K/day | Recommended     |
| **Zerodha Kite API** | NSE/BSE      | ₹2,000/month   | ✅ Broker  | Recommended     |
| **5Paisa API**       | NSE/BSE      | ₹3,000/month   | ✅ Limited | Good value      |
| **Angel One API**    | NSE/BSE      | ₹2,500/month   | ✅ Limited | Good value      |
| **AlgoJi**           | NSE/BSE      | ₹500/month     | ✅ Basic   | Budget-friendly |
| **Shoonya API**      | NSE/BSE      | Free           | ✅ Full    | Open source     |
| **Google Finance**   | NSE/BSE      | Free           | ✅ Full    | Limited data    |
| **yfinance**         | NSE/BSE      | Free           | ✅ Full    | Basic data      |

---

## Application Resource Requirements

### Current Local Setup

```
Memory:        6GB allocated
CPU:           2 cores reserved
Storage:       ~500MB (SQLite)
Network:       Minimal (local testing)
```

### Projected Production Usage (Penny Stocks)

```
API Requests:      ~1,000-5,000 per day
Dashboard Views:   ~10-50 per day
Data Processing:   Batch jobs (hourly)
Database Size:     ~2GB (first year)
```

---

## 💰 INDIA API CONSUMPTION COSTS (Monthly in ₹)

### Scenario 1: Small Deployment (100 stocks, 1,000 API calls/day)

**Data Provider Recommendation: Shoonya API (Free) + AlgoJi Backup**

| Component                    | Cost (₹)   | Notes                   |
| ---------------------------- | ---------- | ----------------------- |
| **Market Data API**          |            |                         |
| Shoonya (NSE/BSE Live)       | ₹0         | Free, fully functional  |
| AlgoJi Backup (alternate)    | ₹500       | For redundancy          |
|                              |            |                         |
| **Cloud Infrastructure**     |            |                         |
| AWS ECS Fargate (API)        | ₹1,500     | 1 vCPU, 2GB × 730 hrs   |
| RDS PostgreSQL (db.t3.small) | ₹3,750     | Multi-AZ, backups       |
| S3 Storage + Transfer        | ₹750       | Historical data storage |
| CloudWatch Logs              | ₹700       | Monitoring & debugging  |
|                              |            |                         |
| **Total Monthly Cost**       | **₹7,200** |                         |

**Annual Cost**: ₹86,400

### Scenario 2: Medium Deployment (500 stocks, 10,000 API calls/day)

**Data Provider Recommendation: Zerodha Kite API + Shoonya**

| Component                     | Cost (₹)    | Notes                          |
| ----------------------------- | ----------- | ------------------------------ |
| **Market Data API**           |             |                                |
| Zerodha Kite API (Broker)     | ₹2,000      | 50,000 calls/day free tier     |
| Shoonya (Backup)              | ₹0          | Free backup                    |
| Historical Data (5Paisa)      | ₹1,500      | Deep historical + F&O          |
|                               |             |                                |
| **Cloud Infrastructure**      |             |                                |
| AWS ECS Fargate (2 tasks)     | ₹3,000      | 1 vCPU × 2, 2GB each × 730 hrs |
| RDS PostgreSQL (db.t3.medium) | ₹7,875      | 100GB storage, 2 DBs           |
| S3 Storage + Transfer         | ₹2,500      | 500GB storage tier             |
| CloudWatch Logs + Metrics     | ₹1,500      | Advanced monitoring            |
| NAT Gateway                   | ₹1,000      | External API calls             |
|                               |             |                                |
| **Total Monthly Cost**        | **₹19,875** |                                |

**Annual Cost**: ₹238,500

### Scenario 3: Large Deployment (2,000+ stocks, 50,000+ API calls/day)

**Data Provider Recommendation: Upstox API + Direct NSE feed**

| Component                 | Cost (₹)    | Notes                     |
| ------------------------- | ----------- | ------------------------- |
| **Market Data API**       |             |                           |
| Upstox API (Professional) | ₹5,000      | Unlimited data calls      |
| Direct NSE Feed           | ₹25,000     | Real-time tick data       |
| Historical & Archive      | ₹2,000      | Backup data source        |
|                           |             |                           |
| **Cloud Infrastructure**  |             |                           |
| AWS ECS Fargate (4 tasks) | ₹7,500      | 1 vCPU × 4, Auto-scaling  |
| RDS Aurora PostgreSQL     | ₹20,000     | db.r5.large, 200GB, HA    |
| RDS Read Replica          | ₹10,000     | For high throughput       |
| S3 + Glacier Archive      | ₹5,000      | 2TB storage + tiering     |
| ElastiCache Redis         | ₹2,000      | In-memory caching         |
| CloudWatch + X-Ray        | ₹3,500      | Full monitoring + tracing |
| NAT Gateway + ALB         | ₹3,000      | High-traffic routing      |
| Data Transfer             | ₹2,000      | Outbound API traffic      |
|                           |             |                           |
| **Total Monthly Cost**    | **₹85,000** |                           |

**Annual Cost**: ₹1,020,000

---

## AWS India Pricing in Rupees

### Scenario 1: Development/Test Environment

**Infrastructure**:

- **Compute**: 1x ECS task (1 vCPU, 2GB memory)
- **Load Balancer**: ALB (minimal usage)
- **Database**: RDS PostgreSQL (db.t3.small)
- **Storage**: S3 (100GB standard)

**Monthly Cost Breakdown**:

| Component               | Details                   | Monthly Cost | INR (₹)    |
| ----------------------- | ------------------------- | ------------ | ---------- |
| **ECS Fargate Compute** | 0.5 vCPU, 2GB × 730 hrs   | $18.25       | ₹1,515     |
| **RDS PostgreSQL**      | db.t3.small, 20GB storage | $45.00       | ₹3,735     |
| **RDS Backup Storage**  | Automated backups         | $5.00        | ₹415       |
| **ALB**                 | 1 ALB, minimal data       | $12.00       | ₹996       |
| **CloudWatch Logs**     | ~2GB/month ingestion      | $8.50        | ₹706       |
| **Data Transfer (OUT)** | ~10GB/month               | $1.50        | ₹125       |
| **S3 Storage**          | 50GB cold storage         | $1.00        | ₹83        |
| **NAT Gateway**         | Minimal traffic           | $0           | ₹0         |
| **Route 53**            | 1 hosted zone             | $0.50        | ₹42        |
| **Miscellaneous**       | Secrets Manager, etc      | $2.00        | ₹166       |
| **Total**               |                           | **$93.75**   | **₹7,783** |

**With 20% buffer/overages**: **$112-120/month = ₹9,296-9,960/month**

**India-focused**: This includes NSE/BSE market data APIs (Shoonya Free tier)

---

### Scenario 2: Production (Small Scale)

**Infrastructure**:

- **Compute**: 2x ECS tasks (1 vCPU each, 2GB memory)
- **Load Balancer**: ALB with health checks
- **Database**: RDS PostgreSQL (db.t3.medium)
- **Storage**: S3 (500GB) + EBS (20GB)
- **Monitoring**: Enhanced CloudWatch

**Monthly Cost Breakdown**:

| Component                    | Details                         | Monthly Cost |
| ---------------------------- | ------------------------------- | ------------ |
| **ECS Fargate Compute**      | 1 vCPU, 2GB × 2 tasks × 730 hrs | $36.50       |
| **RDS PostgreSQL**           | db.t3.medium, 100GB storage     | $95.00       |
| **RDS Multi-AZ**             | High availability               | $95.00       |
| **RDS Backup Storage**       | 30-day retention                | $15.00       |
| **RDS Enhanced Monitoring**  | Detailed metrics                | $5.00        |
| **ALB**                      | 1 ALB, moderate traffic         | $18.00       |
| **ALB Data Processing**      | 100GB/month                     | $10.00       |
| **CloudWatch Logs**          | ~5GB/month ingestion            | $21.25       |
| **CloudWatch Metrics**       | Custom metrics                  | $10.00       |
| **Auto Scaling**             | CPU/Memory based scaling        | $0           |
| **Data Transfer (OUT)**      | ~50GB/month (API)               | $7.50        |
| **S3 Storage**               | 500GB standard + 100GB archive  | $15.00       |
| **S3 Data Transfer**         | Archive retrieval               | $2.50        |
| **NAT Gateway**              | External API calls              | $15.00       |
| **Route 53**                 | DNS queries, health checks      | $5.00        |
| **Secrets Manager**          | 1 secret + rotations            | $1.00        |
| **Lambda (data collection)** | ~1M invocations/month           | $10.00       |
| **Miscellaneous**            | SNS, SQS for notifications      | $5.00        |
| **Total**                    |                                 | **$361.75**  |

**With 20% buffer/overages**: **$430-450/month**

---

### Scenario 3: Production (Scale for Growth)

**Infrastructure**:

- **Compute**: 4x ECS tasks (1 vCPU, 2GB memory) + Auto Scaling
- **Load Balancer**: ALB + CloudFront (CDN)
- **Database**: RDS PostgreSQL (db.r5.large) + Read Replica
- **Storage**: S3 (2TB) + Backup vault
- **Caching**: ElastiCache Redis (cache.t3.small)

**Monthly Cost Breakdown**:

| Component                   | Details                         | Monthly Cost  |
| --------------------------- | ------------------------------- | ------------- |
| **ECS Fargate Compute**     | 1 vCPU, 2GB × 4 tasks × 730 hrs | $73.00        |
| **RDS PostgreSQL**          | db.r5.large, 200GB storage      | $285.00       |
| **RDS Read Replica**        | In same region                  | $285.00       |
| **RDS Multi-AZ**            | Primary + standby               | $0 (included) |
| **RDS Backup Storage**      | 30-day retention                | $30.00        |
| **RDS Enhanced Monitoring** | Detailed metrics                | $10.00        |
| **ElastiCache Redis**       | cache.t3.small, 1GB             | $25.00        |
| **ALB**                     | 1 ALB, high traffic             | $20.00        |
| **ALB Data Processing**     | 500GB/month                     | $50.00        |
| **CloudFront**              | CDN, 1TB/month transfer         | $85.00        |
| **CloudWatch Logs**         | ~20GB/month ingestion           | $85.00        |
| **CloudWatch Metrics**      | Custom dashboards               | $20.00        |
| **Data Transfer (OUT)**     | ~200GB/month via ALB            | $30.00        |
| **S3 Storage**              | 1TB standard + 1TB archive      | $50.00        |
| **S3 Data Transfer**        | 100GB retrieval                 | $15.00        |
| **NAT Gateway**             | Heavy external API calls        | $45.00        |
| **Route 53**                | Advanced health checks          | $10.00        |
| **Secrets Manager**         | Multiple secrets                | $3.00         |
| **Lambda (daily jobs)**     | ~3M invocations/month           | $30.00        |
| **SQS**                     | Task queues, 10M msgs/month     | $5.00         |
| **SNS**                     | Email notifications             | $3.00         |
| **CloudFormation**          | Infrastructure templates        | $0            |
| **Miscellaneous**           | VPC, Security groups, etc       | $10.00        |
| **Total**                   |                                 | **$1,075.00** |

**With 20% buffer/overages**: **$1,280-1,350/month**

---

## GCP India (Delhi) Region Pricing

### Scenario 1: Development/Test Environment

**Infrastructure**:

- **Compute**: 1x Cloud Run (0.5 vCPU, 512MB memory)
- **Database**: Cloud SQL PostgreSQL (db-f1-micro, shared tier)
- **Storage**: Cloud Storage (100GB standard)

**Monthly Cost Breakdown**:

| Component                | Details                   | Monthly Cost |
| ------------------------ | ------------------------- | ------------ |
| **Cloud Run**            | 0.5 vCPU, 512MB × 730 hrs | $14.60       |
| **Cloud Run Requests**   | 10K requests/month        | $0.50        |
| **Cloud SQL PostgreSQL** | db-f1-micro, shared tier  | $35.00       |
| **Cloud SQL Storage**    | 20GB                      | $5.00        |
| **Cloud SQL Backups**    | Automated backups         | $2.00        |
| **Cloud Storage**        | 50GB standard class       | $1.00        |
| **Cloud Storage Egress** | 10GB/month                | $1.50        |
| **Cloud Logging**        | 2GB/month ingestion       | $5.00        |
| **Cloud Monitoring**     | Basic metrics             | $3.00        |
| **Cloud DNS**            | 1 zone                    | $0.20        |
| **Artifact Registry**    | 100GB image storage       | $0.50        |
| **Miscellaneous**        | VPC, IAM, etc             | $1.00        |
| **Total**                |                           | **$69.30**   |

**With 20% buffer/overages**: **$83-100/month**

**Note**: GCP appears cheaper for dev/test due to shared DB tier and Cloud Run's pay-per-request model.

---

### Scenario 2: Production (Small Scale)

**Infrastructure**:

- **Compute**: 2x Cloud Run instances (1 vCPU, 2GB memory)
- **Load Balancer**: Cloud Load Balancing
- **Database**: Cloud SQL PostgreSQL (db-custom-2-8192)
- **Storage**: Cloud Storage (500GB)
- **Caching**: Memorystore Redis (1GB)

**Monthly Cost Breakdown**:

| Component                | Details                             | Monthly Cost |
| ------------------------ | ----------------------------------- | ------------ |
| **Cloud Run**            | 1 vCPU, 2GB × 2 instances × 730 hrs | $73.00       |
| **Cloud Run Requests**   | 100K requests/month                 | $0.50        |
| **Cloud SQL PostgreSQL** | db-custom-2-8192, 100GB             | $140.00      |
| **Cloud SQL HA Replica** | For redundancy                      | $70.00       |
| **Cloud SQL Backups**    | 30-day retention                    | $10.00       |
| **Memorystore Redis**    | 1GB, Standard tier                  | $45.00       |
| **Cloud Load Balancing** | 1 LB, 100GB traffic                 | $35.00       |
| **Cloud Storage**        | 500GB standard                      | $10.00       |
| **Cloud Storage Egress** | 50GB/month                          | $7.50        |
| **Cloud Logging**        | 5GB/month ingestion                 | $12.50       |
| **Cloud Monitoring**     | Custom metrics                      | $5.00        |
| **Cloud Trace**          | Distributed tracing                 | $1.00        |
| **Cloud DNS**            | DNS queries                         | $0.50        |
| **Artifact Registry**    | 500GB image storage                 | $5.00        |
| **Service Accounts**     | 5 service accounts                  | $0           |
| **Cloud Functions**      | ~1M invocations/month               | $2.00        |
| **Cloud Pub/Sub**        | 10M messages/month                  | $3.00        |
| **Miscellaneous**        | VPC, Firewall rules, etc            | $5.00        |
| **Total**                |                                     | **$425.00**  |

**With 20% buffer/overages**: **$510-540/month**

---

### Scenario 3: Production (Scale for Growth)

**Infrastructure**:

- **Compute**: 4x Cloud Run instances (2 vCPU, 4GB memory) + Auto Scaling
- **Load Balancer**: Cloud Load Balancing + Cloud CDN
- **Database**: Cloud SQL PostgreSQL (db-custom-4-16384) + Read Replica
- **Storage**: Cloud Storage (2TB) + Backup
- **Caching**: Memorystore Redis (4GB)

**Monthly Cost Breakdown**:

| Component                  | Details                             | Monthly Cost  |
| -------------------------- | ----------------------------------- | ------------- |
| **Cloud Run**              | 2 vCPU, 4GB × 4 instances × 730 hrs | $292.00       |
| **Cloud Run Requests**     | 500K requests/month                 | $2.50         |
| **Cloud SQL PostgreSQL**   | db-custom-4-16384, 200GB            | $280.00       |
| **Cloud SQL HA Replica**   | Primary + standby                   | $280.00       |
| **Cloud SQL Read Replica** | In same region                      | $140.00       |
| **Cloud SQL Backups**      | 30-day retention                    | $20.00        |
| **Memorystore Redis**      | 4GB, Standard tier                  | $180.00       |
| **Cloud Load Balancing**   | 1 LB, 500GB traffic                 | $45.00        |
| **Cloud CDN**              | 1TB/month cache traffic             | $85.00        |
| **Cloud Storage**          | 1TB standard + 1TB archive          | $50.00        |
| **Cloud Storage Egress**   | 200GB/month                         | $30.00        |
| **Cloud Logging**          | 20GB/month ingestion                | $50.00        |
| **Cloud Monitoring**       | Advanced dashboards                 | $20.00        |
| **Cloud Trace**            | Detailed tracing                    | $5.00         |
| **Cloud Profiler**         | Continuous profiling                | $3.00         |
| **Cloud DNS**              | Advanced DNS features               | $1.00         |
| **Artifact Registry**      | 2TB image storage                   | $50.00        |
| **Cloud Functions**        | ~3M invocations/month               | $6.00         |
| **Cloud Pub/Sub**          | 50M messages/month                  | $15.00        |
| **Cloud Tasks**            | Job scheduling                      | $2.00         |
| **Cloud Scheduler**        | Cron jobs                           | $0.50         |
| **Miscellaneous**          | VPC, Firewall, IAM, etc             | $10.00        |
| **Total**                  |                                     | **$1,368.00** |

**With 20% buffer/overages**: **$1,640-1,750/month**

---

## Cost Comparison Summary

### Monthly Costs (USD)

```
┌─────────────────────┬──────────┬─────────┬──────────┐
│ Scenario            │ AWS Low  │ GCP Low │ Savings  │
├─────────────────────┼──────────┼─────────┼──────────┤
│ Dev/Test            │ $120     │ $100    │ GCP +20% │
│ Production (Small)  │ $450     │ $540    │ AWS +20% │
│ Production (Scale)  │ $1,350   │ $1,750  │ AWS +30% │
└─────────────────────┴──────────┴─────────┴──────────┘
```

### Annual Costs (USD)

```
┌─────────────────────┬──────────┬─────────┬──────────┐
│ Scenario            │ AWS      │ GCP     │ Savings  │
├─────────────────────┼──────────┼─────────┼──────────┤
│ Dev/Test            │ $1,440   │ $1,200  │ GCP +20% │
│ Production (Small)  │ $5,400   │ $6,480  │ AWS +20% │
│ Production (Scale)  │ $16,200  │ $21,000 │ AWS +30% │
└─────────────────────┴──────────┴─────────┴──────────┘
```

---

## Detailed Cost Drivers & Optimization

### AWS Cost Drivers

1. **RDS Database**: Biggest expense (30-40% of cost)

   - **Optimization**: Use Aurora Serverless (40% savings), or switch to DynamoDB
   - **Savings**: $95 → $50/month for small scale

2. **Compute**: ECS/Fargate

   - **Optimization**: Use Spot instances (70% discount), or Lambda for APIs
   - **Savings**: $36 → $15/month

3. **Data Transfer**: Egress charges
   - **Optimization**: CloudFront CDN (50% bandwidth reduction)
   - **Savings**: $30 → $15/month for small scale

**Optimized AWS Small Production**: $300-350/month

### GCP Cost Drivers

1. **Compute**: Cloud Run is expensive at scale

   - **Optimization**: Use GKE with committed discounts (40% off)
   - **Savings**: $73 → $40/month for small scale

2. **Cloud SQL Database**: Similar to AWS

   - **Optimization**: Use Firestore/Datastore for non-relational data
   - **Savings**: $140 → $80/month

3. **Memorystore**: Redis pricing
   - **Optimization**: Use built-in caching layers
   - **Savings**: $45 → $0/month if not needed

**Optimized GCP Small Production**: $350-400/month

---

## Regional Pricing Comparison: India vs Other Regions

### AWS Pricing per Region (for Small Production scenario)

| Region                    | DB Instance | Compute | Total | vs India |
| ------------------------- | ----------- | ------- | ----- | -------- |
| **India (ap-south-1)**    | $95         | $36.50  | $450  | Baseline |
| **Singapore**             | $110        | $39     | $480  | +7%      |
| **Tokyo**                 | $105        | $38     | $470  | +4%      |
| **US East (N. Virginia)** | $90         | $34     | $420  | -7%      |

**Note**: India region is competitive but ~5-10% more expensive than US regions due to lower operational costs in US.

### GCP Pricing per Region (for Small Production scenario)

| Region            | Cloud SQL | Cloud Run | Total | vs India |
| ----------------- | --------- | --------- | ----- | -------- |
| **India (delhi)** | $140      | $73       | $540  | Baseline |
| **Singapore**     | $150      | $75       | $565  | +5%      |
| **Tokyo**         | $145      | $74       | $558  | +3%      |
| **US Central**    | $120      | $65       | $480  | -11%     |

---

## Recommended Deployment Architecture for Cost Optimization

### Recommended Hybrid Approach (AWS)

**Monthly Cost: $320-380/month**

```
1. Compute: ECS Fargate (on-demand + Spot mix)
   - Peak hours: On-demand (2 tasks)
   - Off-peak: Spot (1 task) - 70% discount
   Estimated: $20/month

2. Database: RDS Aurora PostgreSQL Serverless
   - Auto-scaling based on connections
   - Pay per second
   Estimated: $50/month

3. Caching: ElastiCache Redis (shared)
   - Small cache.t3.micro instance
   Estimated: $12/month

4. Storage: S3 + Intelligent-Tiering
   - Automatic archival after 30 days
   Estimated: $5/month

5. CDN: CloudFront
   - Cache prediction results
   - Reduce compute costs
   Estimated: $20/month

6. Monitoring & Logs: CloudWatch
   - Log aggregation + dashboards
   Estimated: $15/month

7. Networking: NAT Gateway + ALB
   - Minimal for internal traffic
   Estimated: $12/month

Total: $134/month base + overages = ~$320-380/month
```

---

## Cost Estimation by Use Case

### Use Case 1: Personal/Research (Low Traffic)

**Expected**: 10-50 requests/day, 1-2 concurrent users

| Provider   | Setup                                       | Monthly | Annual   |
| ---------- | ------------------------------------------- | ------- | -------- |
| **AWS**    | Serverless (Lambda + RDS Aurora Serverless) | $50-80  | $600-960 |
| **GCP**    | Cloud Run + Cloud SQL shared                | $40-60  | $480-720 |
| **Winner** | **GCP** ✅                                  | **$50** | **$600** |

### Use Case 2: Small Business (Moderate Traffic)

**Expected**: 100-500 requests/day, 5-10 concurrent users, 25 stocks

| Provider   | Setup                             | Monthly  | Annual       |
| ---------- | --------------------------------- | -------- | ------------ |
| **AWS**    | Optimized (Fargate + Aurora)      | $300-350 | $3,600-4,200 |
| **GCP**    | Optimized (Cloud Run + Cloud SQL) | $350-400 | $4,200-4,800 |
| **Winner** | **AWS** ✅                        | **$320** | **$3,840**   |

### Use Case 3: Commercial SaaS (High Traffic)

**Expected**: 10K+ requests/day, 100+ concurrent users, Multiple portfolios

| Provider   | Setup                              | Monthly      | Annual         |
| ---------- | ---------------------------------- | ------------ | -------------- |
| **AWS**    | Optimized (GKE-style + RDS Aurora) | $1,000-1,200 | $12,000-14,400 |
| **GCP**    | GKE + Cloud SQL                    | $900-1,100   | $10,800-13,200 |
| **Winner** | **GCP** ✅                         | **$1,000**   | **$12,000**    |

---

## Implementation Timeline & Migration Costs

### Week 1-2: Infrastructure Setup

**AWS Setup**:

- Create VPC, RDS instance, ECS cluster
- Configure ALB, CloudFront
- Setup CI/CD pipeline
- **Time**: 40-60 hours
- **Cost**: $0 (management time)

**GCP Setup**:

- Create VPC, Cloud SQL, Cloud Run
- Configure Load Balancer, CDN
- Setup CI/CD pipeline
- **Time**: 35-50 hours (simpler)
- **Cost**: $0 (management time)

### Week 3: Migration & Testing

**Data Migration**:

- Backup local SQLite → PostgreSQL
- Validate data integrity
- **Time**: 10-15 hours
- **Cost**: $0

**Application Deployment**:

- Containerize (Docker)
- Deploy API + Dashboard
- Run smoke tests
- **Time**: 15-20 hours
- **Cost**: $0

### Week 4: Optimization & Monitoring

**Cost Optimization**:

- Implement caching
- Setup CloudFront/CDN
- Configure auto-scaling
- **Time**: 20-30 hours

**Monitoring Setup**:

- CloudWatch/Cloud Monitoring dashboards
- Alert configuration
- Log aggregation
- **Time**: 10-15 hours

**One-Time Migration Costs**: $0 (internal labor ~100 hours)

---

## Break-Even Analysis

### Current Local Setup (Free)

```
Investment: 0
Monthly: $0
Annual: $0
```

### AWS Production Deployment

```
Initial Setup: $2,000 (infrastructure + migration labor)
Monthly: $320-450 (optimized small scale)
Annual: $3,840-5,400

Break-even: Less than 1 month
Break-even w/ setup: ~2 months
```

### GCP Production Deployment

```
Initial Setup: $1,500 (simpler setup)
Monthly: $350-400 (optimized small scale)
Annual: $4,200-4,800

Break-even: Less than 1 month
Break-even w/ setup: ~2 months
```

---

## Cost Reduction Strategies

### Short-term (0-3 months)

1. **Use Spot/Preemptible Instances**

   - AWS Spot: 70% discount on compute
   - GCP Preemptible: 80% discount
   - **Savings**: $100-200/month

2. **Database Optimization**

   - Implement query caching
   - Add indexes for common queries
   - **Savings**: $20-50/month

3. **CDN & Compression**
   - CloudFront/Cloud CDN
   - Gzip API responses
   - **Savings**: $30-80/month

**Total Short-term Savings**: $150-330/month

### Medium-term (3-6 months)

1. **Serverless Architecture**

   - Migrate APIs to Lambda/Cloud Functions
   - Pay only for execution time
   - **Savings**: $150-300/month

2. **Database Scaling**

   - Aurora Serverless (AWS) or Firestore (GCP)
   - Pay per query, not per instance
   - **Savings**: $100-200/month

3. **Data Pipeline Optimization**
   - Batch processing instead of real-time
   - Off-peak execution
   - **Savings**: $50-100/month

**Total Medium-term Savings**: $300-600/month

### Long-term (6+ months)

1. **Reserved Instances/Commitments**

   - 1-year commitment: 30% discount
   - 3-year commitment: 50% discount
   - **Savings**: $200-400/month

2. **Multi-region Optimization**

   - Distribute traffic across cheaper regions
   - Data residency optimization
   - **Savings**: $100-300/month

3. **Custom Infrastructure**
   - Consider bare metal or dedicated hosts
   - Only if scaling to 10K+ requests/day
   - **Savings**: $500+/month

**Total Long-term Savings**: $300-700/month

---

## Final Recommendation

### For Stock Analyzer MVP (Penny Stocks)

**Best Option: AWS India (Mumbai)**

**Rationale**:

1. ✅ 15-20% cheaper than GCP for small-medium scale
2. ✅ Better RDS optimization options
3. ✅ More mature Spot instance market
4. ✅ Excellent support for Python/FastAPI
5. ✅ Cost predictability

**Recommended Setup**:

```
Compute:      ECS Fargate (1-2 tasks)
Database:     RDS Aurora Serverless PostgreSQL
Cache:        ElastiCache Redis (optional)
Storage:      S3 with intelligent-tiering
CDN:          CloudFront
Monitoring:   CloudWatch Logs + Metrics

Monthly Cost: $300-400
Annual Cost:  $3,600-4,800
```

**Cost-Optimized Deployment**:

```
Compute:      Lambda + API Gateway (pay-per-request)
Database:     Aurora Serverless (pay-per-second)
Storage:      S3 standard
Monitoring:   Basic CloudWatch

Monthly Cost: $150-250
Annual Cost:  $1,800-3,000
```

---

## Appendix: Service Availability & SLA

### AWS India (Mumbai) Availability

- **Region**: ap-south-1
- **Availability Zones**: 3
- **SLA**: 99.99% for RDS, 99.95% for ECS
- **Support**: 24/7 via AWS Support

### GCP India (Delhi) Availability

- **Region**: asia-south1
- **Availability Zones**: 3
- **SLA**: 99.95% for Cloud SQL, 99.95% for Cloud Run
- **Support**: 24/7 via Google Cloud Support

**Both regions have excellent availability and compliance for Indian data.**

---

## Next Steps

1. **Start with AWS** (15-20% cheaper for this use case)
2. **Use Serverless First** (Lambda + Aurora Serverless)
3. **Monitor spending** with CloudWatch cost anomaly detection
4. **Optimize monthly** based on actual usage patterns
5. **Review quarterly** for cost reduction opportunities

**Timeline to Production**: 2-4 weeks
**Time to Profitability**: Depends on monetization model
