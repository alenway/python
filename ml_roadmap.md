# AI / ML / DL + SQL — The Complete Roadmap

> **Philosophy:** AI/ML is not a linear path you "finish." It is a continuous loop:
> `Define → Collect → Process → Train → Evaluate → Deploy → Monitor → Retrain → Repeat`

---

# PART A — SQL ROADMAP

> SQL is the language of data. Before you touch any ML model, you must be able to query, transform, and understand your data.

---

## SQL Level 1 — Core Foundations

### What is SQL?

- SQL (Structured Query Language) is used to communicate with relational databases
- Every data science and ML role expects proficiency in SQL
- Databases: PostgreSQL (recommended), MySQL, SQLite, SQL Server

### Basic Querying

```sql
SELECT column1, column2
FROM table_name
WHERE condition
ORDER BY column1 ASC
LIMIT 10;
```

- `SELECT` — choose columns
- `FROM` — choose table
- `WHERE` — filter rows
- `ORDER BY` — sort results (ASC / DESC)
- `LIMIT` — restrict number of rows
- `DISTINCT` — remove duplicates

### Filtering & Conditions

- Comparison operators: `=`, `!=`, `>`, `<`, `>=`, `<=`
- Logical operators: `AND`, `OR`, `NOT`
- Range: `BETWEEN ... AND ...`
- List: `IN (val1, val2, ...)`
- Pattern: `LIKE '%keyword%'`
- Null checks: `IS NULL`, `IS NOT NULL`

### Sorting & Limiting

- `ORDER BY col ASC/DESC`
- `LIMIT n OFFSET m` — pagination

---

## SQL Level 2 — Aggregations & Grouping

### Aggregate Functions

| Function                | Purpose             |
| ----------------------- | ------------------- |
| `COUNT(*)`              | Count total rows    |
| `COUNT(DISTINCT col)`   | Count unique values |
| `SUM(col)`              | Sum of values       |
| `AVG(col)`              | Average             |
| `MIN(col)` / `MAX(col)` | Minimum / Maximum   |

### GROUP BY & HAVING

```sql
SELECT department, COUNT(*) AS employee_count, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000
ORDER BY avg_salary DESC;
```

- `GROUP BY` — groups rows sharing a value
- `HAVING` — filters after grouping (like `WHERE` but for aggregations)
- Rule: every column in `SELECT` must be in `GROUP BY` or inside an aggregate function

### CASE Statements (conditional logic)

```sql
SELECT name, salary,
  CASE
    WHEN salary > 100000 THEN 'Senior'
    WHEN salary > 60000  THEN 'Mid-level'
    ELSE 'Junior'
  END AS level
FROM employees;
```

---

## SQL Level 3 — Joins (Most Critical Skill)

### Types of Joins

```
Table A    Table B
  [1,2,3]    [2,3,4]

INNER JOIN  → [2,3]      (only matching rows from both)
LEFT JOIN   → [1,2,3]    (all of A, matching from B or NULL)
RIGHT JOIN  → [2,3,4]    (all of B, matching from A or NULL)
FULL JOIN   → [1,2,3,4]  (all rows from both, NULL where no match)
CROSS JOIN  → Cartesian product (every row × every row)
```

```sql
-- INNER JOIN example
SELECT o.order_id, c.customer_name, o.total
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
WHERE o.total > 500;

-- LEFT JOIN to find customers with NO orders
SELECT c.customer_name
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
WHERE o.order_id IS NULL;
```

### Self Joins

```sql
-- Find employees and their managers (same table)
SELECT e.name AS employee, m.name AS manager
FROM employees e
JOIN employees m ON e.manager_id = m.id;
```

---

## SQL Level 4 — Subqueries & CTEs

### Subqueries

```sql
-- Inline subquery
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Subquery in FROM (derived table)
SELECT dept, avg_sal
FROM (
  SELECT department AS dept, AVG(salary) AS avg_sal
  FROM employees
  GROUP BY department
) AS dept_stats
WHERE avg_sal > 70000;
```

### CTEs (Common Table Expressions) — preferred over subqueries

```sql
WITH high_earners AS (
  SELECT department, AVG(salary) AS avg_sal
  FROM employees
  GROUP BY department
),
top_departments AS (
  SELECT department
  FROM high_earners
  WHERE avg_sal > 80000
)
SELECT e.name, e.department
FROM employees e
JOIN top_departments t ON e.department = t.department;
```

- CTEs make complex queries readable and reusable
- Can be chained: one CTE can reference another

### Recursive CTEs

```sql
-- Traverse a hierarchy (org charts, trees)
WITH RECURSIVE org_tree AS (
  SELECT id, name, manager_id, 1 AS level
  FROM employees
  WHERE manager_id IS NULL   -- start at the root (CEO)

  UNION ALL

  SELECT e.id, e.name, e.manager_id, ot.level + 1
  FROM employees e
  JOIN org_tree ot ON e.manager_id = ot.id
)
SELECT * FROM org_tree ORDER BY level;
```

---

## SQL Level 5 — Window Functions _(most powerful SQL feature for analytics)_

### What Are Window Functions?

Unlike `GROUP BY` which collapses rows, window functions **add a calculated column without reducing rows**.

```sql
SELECT
  name,
  department,
  salary,
  AVG(salary) OVER (PARTITION BY department) AS dept_avg,
  salary - AVG(salary) OVER (PARTITION BY department) AS diff_from_avg,
  RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS salary_rank
FROM employees;
```

### Key Window Functions

| Function                         | Purpose                            |
| -------------------------------- | ---------------------------------- |
| `ROW_NUMBER()`                   | Unique row number within partition |
| `RANK()`                         | Rank with gaps (1,1,3)             |
| `DENSE_RANK()`                   | Rank without gaps (1,1,2)          |
| `NTILE(n)`                       | Divide into n equal buckets        |
| `LAG(col, n)`                    | Value from n rows before           |
| `LEAD(col, n)`                   | Value from n rows ahead            |
| `SUM() OVER (...)`               | Running total                      |
| `FIRST_VALUE()` / `LAST_VALUE()` | First/last value in window         |

```sql
-- Running total (cumulative sum)
SELECT date, revenue,
  SUM(revenue) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_revenue
FROM sales;

-- Month-over-month comparison using LAG
SELECT month, revenue,
  LAG(revenue, 1) OVER (ORDER BY month) AS prev_month,
  revenue - LAG(revenue, 1) OVER (ORDER BY month) AS growth
FROM monthly_sales;
```

---

## SQL Level 6 — Advanced Topics

### Indexes & Performance

- `CREATE INDEX idx_name ON table(column)` — speeds up lookups
- Composite indexes: `CREATE INDEX ON orders(customer_id, created_at)`
- `EXPLAIN` / `EXPLAIN ANALYZE` — see query execution plan
- Avoid `SELECT *` in production
- Index columns used in `WHERE`, `JOIN ON`, and `ORDER BY`

### Data Types & Casting

- Common types: `INT`, `BIGINT`, `FLOAT`, `DECIMAL(10,2)`, `VARCHAR(255)`, `TEXT`, `BOOLEAN`, `DATE`, `TIMESTAMP`, `JSONB`
- Casting: `CAST(column AS INT)` or `column::INT` (PostgreSQL)

### String Functions

```sql
UPPER(str), LOWER(str), LENGTH(str)
TRIM(str), LTRIM(str), RTRIM(str)
SUBSTRING(str FROM 1 FOR 3)
CONCAT(str1, ' ', str2)
REPLACE(str, 'old', 'new')
SPLIT_PART(str, '.', 1)        -- PostgreSQL
```

### Date & Time Functions

```sql
NOW(), CURRENT_DATE, CURRENT_TIMESTAMP
DATE_TRUNC('month', timestamp)           -- truncate to month start
EXTRACT(YEAR FROM date_col)              -- extract year
AGE(timestamp1, timestamp2)             -- difference
timestamp + INTERVAL '7 days'           -- date arithmetic
TO_CHAR(date_col, 'YYYY-MM')            -- format as string
```

### JSON in SQL (PostgreSQL)

```sql
-- Query JSON fields
SELECT data->>'name' AS name,
       data->'address'->>'city' AS city
FROM users;

-- Filter by JSON key
WHERE data->>'status' = 'active'
```

### Transactions & ACID

```sql
BEGIN;
  UPDATE accounts SET balance = balance - 500 WHERE id = 1;
  UPDATE accounts SET balance = balance + 500 WHERE id = 2;
COMMIT;   -- or ROLLBACK on error
```

- **ACID:** Atomicity, Consistency, Isolation, Durability
- Use transactions for operations that must succeed or fail together

### Views & Materialized Views

```sql
-- View (virtual table, runs query on demand)
CREATE VIEW active_customers AS
SELECT * FROM customers WHERE status = 'active';

-- Materialized View (stores result, must refresh)
CREATE MATERIALIZED VIEW monthly_summary AS
SELECT DATE_TRUNC('month', created_at), COUNT(*), SUM(amount)
FROM orders GROUP BY 1;

REFRESH MATERIALIZED VIEW monthly_summary;
```

---

## SQL Level 7 — SQL for Data Science & ML

### Exploratory Data Analysis in SQL

```sql
-- Missing value counts
SELECT
  COUNT(*) AS total_rows,
  COUNT(age) AS non_null_age,
  COUNT(*) - COUNT(age) AS missing_age,
  ROUND(100.0 * (COUNT(*) - COUNT(age)) / COUNT(*), 2) AS pct_missing
FROM users;

-- Distribution / histogram buckets
SELECT
  WIDTH_BUCKET(age, 0, 100, 10) AS age_bucket,
  COUNT(*) AS frequency
FROM users
GROUP BY 1 ORDER BY 1;

-- Percentiles
SELECT
  PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY salary) AS q1,
  PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY salary) AS median,
  PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY salary) AS q3
FROM employees;
```

### Feature Engineering in SQL

```sql
-- One-hot encoding
SELECT
  user_id,
  CASE WHEN category = 'premium' THEN 1 ELSE 0 END AS is_premium,
  CASE WHEN category = 'trial'   THEN 1 ELSE 0 END AS is_trial
FROM users;

-- Binning / Bucketing
SELECT
  user_id,
  CASE
    WHEN age < 25 THEN 'young'
    WHEN age < 45 THEN 'middle'
    ELSE 'senior'
  END AS age_group
FROM users;

-- Lag features for time series
SELECT
  user_id, date, revenue,
  LAG(revenue, 1) OVER (PARTITION BY user_id ORDER BY date) AS revenue_prev_day,
  LAG(revenue, 7) OVER (PARTITION BY user_id ORDER BY date) AS revenue_prev_week
FROM daily_revenue;
```

### SQL Tools Ecosystem

| Tool                      | Purpose                                 |
| ------------------------- | --------------------------------------- |
| **PostgreSQL**            | Best open-source DB — learn this        |
| **DBeaver**               | Free universal SQL GUI                  |
| **pgAdmin**               | PostgreSQL-specific GUI                 |
| **BigQuery**              | Google Cloud SQL at massive scale       |
| **Snowflake**             | Cloud data warehouse                    |
| **dbt (data build tool)** | SQL-based data transformation pipelines |
| **Apache Spark SQL**      | Distributed SQL on big data             |
| **SQLAlchemy**            | Python ↔ SQL bridge                     |

---

# PART B — AI / ML / DL ROADMAP

---

## Stage 0 — Core AI: Python Fundamentals

> The prerequisite programming skills before any data science or ML work.

### Python Basics

- **Variables & Data Types:** int, float, str, bool, list, dict, set, tuple
- **Conditionals:** `if`, `elif`, `else` — control program flow
- **Loops:** `for` loops (iterating sequences), `while` loops (condition-based), list comprehensions
- **Functions:** `def`, parameters, `*args`, `**kwargs`, return values, lambda functions
- **Error Handling:** `try`, `except`, `finally`
- **File I/O:** reading/writing CSV, JSON, text files

### Object-Oriented Programming (OOP)

> Essential for understanding Scikit-Learn, PyTorch, TensorFlow APIs

- **Classes & Objects:** defining classes, instantiation, `__init__`
- **Attributes & Methods:** instance vs class variables
- **Inheritance:** child classes inheriting from parent classes
- **Encapsulation & Polymorphism**
- **Magic Methods:** `__repr__`, `__len__`, `__getitem__`

### Core Libraries (must master before ML)

| Library        | Purpose                                                |
| -------------- | ------------------------------------------------------ |
| **NumPy**      | Numerical computing — arrays, matrix ops, broadcasting |
| **Pandas**     | Data manipulation — DataFrames, groupby, merge         |
| **Matplotlib** | Base plotting library                                  |
| **Seaborn**    | Statistical visualization (built on Matplotlib)        |
| **Plotly**     | Interactive visualizations                             |

### Python for ML Specifically

- Virtual environments: `venv`, `conda`
- Jupyter Notebooks / JupyterLab
- Type hints (`def fn(x: int) -> str`)
- Generators & iterators (memory-efficient data loading)
- Decorators (used heavily in PyTorch Lightning, FastAPI)

**Resources:** Python.org docs, "Automate the Boring Stuff" (free online), Real Python

---

## Stage 1 — Mathematical Foundations

> You cannot debug a failing model without understanding what's happening underneath.

### Linear Algebra

- Vectors, Matrices, Tensors
- Matrix multiplication, Transpose, Inverse
- Eigenvalues & Eigenvectors (used in PCA)
- Singular Value Decomposition (SVD)
- Dot products & Cosine Similarity (crucial for embeddings)

### Calculus

- Derivatives & Partial Derivatives
- **Chain Rule** — backbone of backpropagation
- Gradient, Jacobian, Hessian
- Optimization landscape: local minima, saddle points, loss surfaces

### Probability & Statistics

- Probability Distributions (Normal, Bernoulli, Poisson, Categorical, etc.)
- Bayes' Theorem & Bayesian Inference
- Expectation, Variance, Covariance
- Maximum Likelihood Estimation (MLE)
- Hypothesis Testing, p-values, Confidence Intervals
- **Information Theory:** Entropy, KL Divergence, Cross-Entropy Loss

### Optimization Theory _(often skipped — do not skip)_

- Convex vs Non-Convex problems
- Gradient Descent, SGD, Mini-batch GD
- **Optimizers:** Momentum, RMSProp, Adam, AdaGrad, AdamW
- Learning Rate Schedules: Warmup, Cosine Annealing, Step Decay
- Lagrange Multipliers (used in SVM)

**Resources:** 3Blue1Brown (YouTube), Khan Academy, "Mathematics for ML" book (free PDF)

---

## Stage 2 — Data Engineering & EDA

> This is ~70–80% of real ML work. Master this before modeling.

### Problem Definition _(always first)_

- What is the goal? (Predict, Classify, Cluster, Generate, Rank)
- What metric defines success?
- What data is available vs what is needed?
- Baseline: what does random or simple guessing achieve?

### Data Collection

- Structured data: databases (SQL), CSVs, spreadsheets
- Unstructured data: text, images, audio, video
- APIs, web scraping (BeautifulSoup, Scrapy, Playwright)
- Synthetic data generation
- Labeling tools: Label Studio, Roboflow, Scale AI

### Exploratory Data Analysis (EDA)

- Shape, dtypes, `.describe()`, `.info()`
- Missing value analysis
- Outlier detection: IQR, Z-score, Isolation Forest
- Distribution plots, histograms, box plots
- Correlation heatmaps
- Class balance analysis

### Data Cleaning

- Handling missing values: mean/median/mode imputation, KNN imputer, `SimpleImputer`
- Duplicate removal, type corrections, datetime parsing
- Inconsistent categories (e.g., "Male", "male", "M" → standardize)
- Noise removal

### Feature Engineering _(where models are won and lost)_

- **Encoding:** One-Hot, Label, Ordinal, Target Encoding
- **Scaling:** StandardScaler, MinMaxScaler, RobustScaler
- **Binning/Bucketing:** age groups, price ranges
- **Interaction Features:** multiplying or combining columns
- **Date/Time Features:** day of week, hour of day, time since event
- **Text Features:** TF-IDF, Bag of Words, N-grams
- **Dimensionality Reduction:** PCA, t-SNE (visualization), UMAP (faster, better structure)

### Handling Class Imbalance

- Oversampling: SMOTE, ADASYN
- Undersampling: Random, Tomek Links
- Class weights in model training
- Use F1, ROC-AUC instead of accuracy for evaluation

### Data Splitting & Validation

- Train / Validation / Test split (80/10/10 or 70/15/15)
- Stratified splits (for imbalanced classes)
- Time-series splits (no data leakage!)
- **K-Fold Cross Validation** — more reliable performance estimates

### Data Pipelines & Versioning

- **DVC** — version datasets and models like Git versions code
- **Apache Airflow, Prefect, ZenML** — pipeline orchestration
- **Great Expectations** — data quality validation

---

## Stage 3 — Classic Machine Learning

### 3A. Supervised Learning

#### Regression (predicting a continuous value)

| Model                         | When to Use                           |
| ----------------------------- | ------------------------------------- |
| Linear Regression             | Simple, interpretable baseline        |
| Polynomial Regression         | Non-linear relationships              |
| Ridge (L2) / Lasso (L1)       | Regularization to prevent overfitting |
| ElasticNet                    | Combines Ridge + Lasso                |
| Decision Tree Regressor       | Non-linear, interpretable             |
| Random Forest Regressor       | Robust, handles noise well            |
| XGBoost / LightGBM / CatBoost | State-of-the-art for tabular data     |

#### Classification (predicting a category)

| Model                         | Notes                                       |
| ----------------------------- | ------------------------------------------- |
| Logistic Regression           | Fast baseline, interpretable, probabilistic |
| Support Vector Machine (SVM)  | Powerful for small datasets, good margin    |
| K-Nearest Neighbors (KNN)     | No training, instance-based, slow at scale  |
| Naive Bayes                   | Great for text classification, fast         |
| Decision Tree                 | Interpretable, prone to overfitting         |
| Random Forest                 | Ensemble method, robust to noise            |
| XGBoost / LightGBM / CatBoost | Best for structured/tabular data            |

### 3B. Unsupervised Learning

| Task                     | Models                                                       |
| ------------------------ | ------------------------------------------------------------ |
| Clustering               | K-Means, DBSCAN, Hierarchical, Gaussian Mixture Models (GMM) |
| Dimensionality Reduction | PCA, UMAP, Autoencoders                                      |
| Anomaly Detection        | Isolation Forest, One-Class SVM, Autoencoders                |
| Association Rules        | Apriori, FP-Growth (market basket analysis)                  |

### Evaluation Metrics

#### Classification Metrics

| Metric                                 | When to Use                              |
| -------------------------------------- | ---------------------------------------- |
| Accuracy                               | Balanced datasets only                   |
| Precision / Recall                     | Imbalanced data, medical/fraud detection |
| F1-Score                               | Balance of Precision + Recall            |
| ROC-AUC                                | Ranking ability across thresholds        |
| Log-Loss                               | Probabilistic predictions                |
| Matthews Correlation Coefficient (MCC) | Severe class imbalance                   |
| Confusion Matrix                       | Visual breakdown of TP/TN/FP/FN          |

#### Regression Metrics

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)
- R² (coefficient of determination), Adjusted R²

### Model Validation Practices

- **Cross-validation:** K-Fold, Stratified K-Fold, Leave-One-Out
- **Train-Test Split** with reproducible random seeds
- **Validation curves** — diagnose over/underfitting
- **Learning curves** — check if more data would help
- Checking for **data leakage** (target-related features leaking into training)

**Library:** Scikit-Learn — the standard for all classic ML in Python

---

## Stage 4 — Deep Learning

### 4.1 Neural Networks & MLPs

#### What Is a Neural Network?

- A model that stacks simple "neurons" in layers to learn patterns through weights and biases
- Each neuron: `output = activation(weight · input + bias)`

#### MLP (Multi-Layer Perceptron)

- Fundamental feedforward architecture
- Three key layer types: **Input layer → Hidden layer(s) → Output layer**
- Each layer is fully connected (dense) to the next
- Depth (number of hidden layers) allows learning complex representations

#### Architecture Decisions

- Number of layers and neurons per layer
- Batch size (trade-off between memory and gradient quality)
- Weight initialization: He initialization (for ReLU), Xavier (for Sigmoid/Tanh)
- Batch Normalization — normalize activations between layers for stable training
- Layer Normalization — preferred in Transformers

### 4.2 Backpropagation _(the engine that drives training)_

Three steps every training iteration:

1. **Forward Pass** — Data flows through the network layer by layer to produce a prediction
2. **Loss Calculation** — A loss function measures how far the prediction is from the actual target
3. **Backward Pass** — The algorithm uses the **Chain Rule** of calculus to propagate the error backward and calculate gradients for each weight

```
Loss → ∂Loss/∂W_last → ∂Loss/∂W_(last-1) → ... → ∂Loss/∂W_first
Each weight is updated: W = W - lr × ∂Loss/∂W
```

- **Vanishing Gradient Problem** — gradients shrink to near zero in deep networks (Sigmoid/Tanh layers)
- **Exploding Gradient Problem** — gradients grow uncontrollably (fixed with gradient clipping)
- Solutions: ReLU activation, residual connections, gradient clipping, careful initialization

### 4.3 Activation Functions

> Introduce non-linearity, allowing networks to learn complex non-linear relationships

| Function       | Formula                 | Use Case                                                          |
| -------------- | ----------------------- | ----------------------------------------------------------------- |
| **ReLU**       | `max(0, x)`             | Most popular for hidden layers — fast, avoids vanishing gradients |
| **Leaky ReLU** | `max(0.01x, x)`         | Avoids "dying ReLU" problem                                       |
| **GELU**       | Smooth approximation    | Used in Transformers (BERT, GPT)                                  |
| **SwiGLU**     | Gated variant           | Modern LLMs (LLaMA) — better than ReLU for deep models            |
| **Sigmoid**    | `1/(1+e^-x)`            | Binary classification output layer                                |
| **Tanh**       | `(e^x-e^-x)/(e^x+e^-x)` | Older networks, zero-centered                                     |
| **Softmax**    | `e^xi / Σe^xj`          | Multi-class output layer                                          |

### 4.4 Loss Functions & Optimization

#### Loss Functions

| Loss                            | Use Case                          |
| ------------------------------- | --------------------------------- |
| Mean Squared Error (MSE)        | Regression                        |
| Mean Absolute Error (MAE)       | Regression, robust to outliers    |
| Binary Cross-Entropy            | Binary classification             |
| Categorical Cross-Entropy       | Multi-class classification        |
| Huber Loss                      | Regression — blend of MSE and MAE |
| Contrastive Loss / Triplet Loss | Embedding learning                |

#### Optimization Algorithms

- **SGD with Momentum** — adds velocity term to escape local minima
- **Adam** — adaptive learning rates, most popular default choice
- **AdamW** — Adam with weight decay, preferred for Transformers
- **RMSProp** — good for RNNs and non-stationary problems
- Gradient clipping — prevent exploding gradients

#### Regularization Techniques

- **Dropout** — randomly zeroes neurons during training (prevents co-adaptation)
- **L1 / L2 Weight Decay** — penalizes large weights
- **Data Augmentation** — artificially expands training data
- **Early Stopping** — halt training when validation loss stops improving
- **Batch Normalization / Layer Normalization** — stabilizes training

### 4.5 Deep Learning Architectures

| Architecture         | Primary Use Case                                   |
| -------------------- | -------------------------------------------------- |
| **ANN / MLP**        | Tabular data, general purpose                      |
| **CNN**              | Images, spatial data                               |
| **RNN / LSTM / GRU** | Sequential data, time series (older approach)      |
| **Transformer**      | Text, images, audio, multi-modal (modern standard) |
| **GNN**              | Graph-structured data (molecules, social networks) |
| **Autoencoder**      | Compression, anomaly detection, denoising          |
| **VAE**              | Generative models with latent space control        |
| **GAN**              | Image/video generation                             |
| **Diffusion Models** | State-of-the-art image/audio generation            |

### 4.6 PyTorch — The Standard Library

```python
import torch
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(784, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, 10)
        )

    def forward(self, x):
        return self.layers(x)

model = SimpleNet()
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
criterion = nn.CrossEntropyLoss()
```

- **Autograd** — automatically computes gradients, no manual backprop
- **`nn.Module`** — base class for all neural networks
- **DataLoader** — batched, shuffled data loading with multi-threading
- **TorchScript / ONNX** — export models for production
- **PyTorch Lightning** — reduces boilerplate for training loops

**Resources:** PyTorch official tutorials, fast.ai, Andrej Karpathy's YouTube channel

---

## Stage 5 — Explore Different Paths

### 5A. Computer Vision (CV)

#### Foundational Architecture — CNN

- **Convolutional layers** — detect features (edges, textures, shapes) via learned filters
- **Pooling layers** — reduce spatial dimensions (MaxPool, AvgPool)
- **Feature maps** — output of convolutions, stack of learned feature detectors
- Classic CNNs: LeNet → AlexNet → VGG → ResNet → EfficientNet

#### Object Detection

- **YOLO (v8, v11)** — real-time, single-pass detection (best for speed)
- **Faster R-CNN** — two-stage, highest accuracy
- **DETR** — Transformer-based detection (end-to-end, no anchors)
- **RT-DETR** — real-time DETR (new, combines speed and accuracy)
- Key concepts: anchor boxes, IoU (Intersection over Union), NMS (Non-Max Suppression)

#### Segmentation

- **Semantic Segmentation** — label every pixel with a class (DeepLab, FCN)
- **Instance Segmentation** — separate each object instance (Mask R-CNN)
- **Panoptic Segmentation** — combines both
- **U-Net** — encoder-decoder architecture, widely used in medical imaging
- **SAM (Segment Anything Model)** — Meta's foundational segmentation model

#### Modern Vision Models

- **ViT (Vision Transformer)** — applies Transformer attention to image patches
- **CLIP** — joint image-text embedding (contrastive learning)
- **BLIP-2** — image captioning and visual Q&A
- **Stable Diffusion / SDXL / DALL-E** — text-to-image generation

#### Libraries & Tools

- **torchvision** — datasets, transforms, pre-trained models
- **OpenCV** — classical computer vision (image processing, video)
- **Albumentations** — fast, flexible image augmentation
- **Roboflow** — dataset management, labeling, augmentation pipeline

---

### 5B. Natural Language Processing (NLP)

#### Text Preprocessing

- Tokenization: splitting text into tokens (words, sub-words, characters)
- Stop word removal, stemming, lemmatization
- Regular expressions for text cleaning
- Libraries: **NLTK**, **spaCy** (production NLP)

#### Word Embeddings

- **Bag of Words / TF-IDF** — sparse, frequency-based representations
- **Word2Vec** — dense vectors, captures semantic similarity (king - man + woman ≈ queen)
- **GloVe** — global co-occurrence statistics
- **FastText** — handles sub-word morphology (works on unseen words)

#### Sequence Models

- **RNN** — processes sequences step-by-step (vanishing gradient issue)
- **LSTM (Long Short-Term Memory)** — gated memory, handles longer sequences
- **GRU** — simpler LSTM alternative, similar performance
- **Seq2Seq + Attention** — precursor to Transformers (machine translation)

#### NLP Tasks

| Task                               | Description                              |
| ---------------------------------- | ---------------------------------------- |
| **NER** (Named Entity Recognition) | Identify names, dates, locations in text |
| **POS Tagging**                    | Label parts of speech (noun, verb, etc.) |
| **Sentiment Analysis**             | Positive / negative / neutral            |
| **Text Classification**            | Categorize documents                     |
| **Machine Translation**            | Translate between languages              |
| **Summarization**                  | Extractive and abstractive               |
| **Question Answering**             | Extract or generate answers              |

**Libraries:** spaCy, Hugging Face `transformers`, NLTK, Gensim

---

### 5C. Reinforcement Learning (RL)

#### Core Framework — MDP (Markov Decision Process)

- **Agent** — the learner/decision maker
- **Environment** — what the agent interacts with
- **State (S)** — current situation
- **Action (A)** — choices available to the agent
- **Reward (R)** — feedback signal (positive or negative)
- **Policy (π)** — the agent's strategy (state → action)

#### Key Algorithms

| Algorithm                              | Type                           | Notes                                        |
| -------------------------------------- | ------------------------------ | -------------------------------------------- |
| Q-Learning                             | Model-free, off-policy         | Tabular, simple environments                 |
| SARSA                                  | Model-free, on-policy          | More conservative than Q-learning            |
| **DQN (Deep Q-Network)**               | Deep RL                        | Q-learning + neural net (Atari games)        |
| **PPO (Proximal Policy Optimization)** | Policy gradient                | Most popular, stable training                |
| A3C / A2C                              | Actor-Critic                   | Parallel training                            |
| **SAC (Soft Actor-Critic)**            | Off-policy, continuous actions | Robotics, physics simulation                 |
| **RLHF**                               | Human feedback                 | How ChatGPT was aligned to human preferences |

**Libraries:** Gymnasium (OpenAI Gym successor), Stable-Baselines3, RLlib (Ray)

---

### 5D. Speech and Audio Processing

#### Key Tasks

- **ASR (Automatic Speech Recognition)** — Speech → Text
  - Models: **Whisper** (OpenAI), Wav2Vec 2.0, DeepSpeech
- **TTS (Text-to-Speech)** — Text → Speech
  - Models: VALL-E, Bark, ElevenLabs API, Tacotron 2
- **Speaker Diarization** — who spoke when?
- **Sound Classification** — classify environmental sounds, music genres
- **Music Generation** — MusicGen (Meta), AudioCraft

#### Feature Extraction for Audio

- **Waveform** — raw time-series amplitude signal
- **Spectrogram** — time vs frequency visualization (Short-Time Fourier Transform)
- **Mel Spectrogram** — frequency on mel scale (closer to human perception)
- **MFCC (Mel-Frequency Cepstral Coefficients)** — compact audio representation
- **Librosa** — Python library for audio analysis

---

## Stage 6 — Transformer Architecture (Deep Dive)

### Why Transformers Changed Everything

- Unlike RNNs that process sequences word-by-word, **Transformers process entire sequences in parallel**
- Introduced in "Attention Is All You Need" (Vaswani et al., 2017)
- Foundation of all modern LLMs (GPT, BERT, LLaMA, Gemini)

### Transformer Data Flow

```
Input Text → Tokenization → Token Embeddings + Positional Embeddings
         ↓
[Encoder Layer] × N
  Multi-Head Self-Attention → Add & Norm → Feed-Forward → Add & Norm
         ↓
[Decoder Layer] × N (for seq2seq models)
  Masked Self-Attention → Cross-Attention → Feed-Forward
         ↓
Output Projection → Softmax → Predicted Token
```

- **Encoder** — takes input sequences and converts them into abstract representations (context vectors)
- **Decoder** — uses encoder representations + previously generated tokens to predict next token
- **Residual Connections** — data "skips" layers, preventing vanishing gradients: `output = layer(x) + x`
- **Layer Normalization** — standardizes activations for stable training

### Positional Embeddings

> Since Transformers process all tokens simultaneously, they have no inherent sense of order.

- **Purpose:** inject information about where each word sits in a sequence
- **Sinusoidal (original):** fixed sine/cosine functions of varying frequencies encode absolute position
- **Learned Positional Embeddings:** trainable vectors added to token embeddings
- **RoPE (Rotary Positional Embeddings):** integrates position directly into Q/K computations — better for long sequences, used in LLaMA, Mistral, GPT-NeoX
- **ALiBi:** attention-based positional bias — allows extrapolation beyond training length

### The Attention Mechanism _(the core of every Transformer)_

For each token, the model computes three vectors:

- **Query (Q)** — "What information am I looking for?"
- **Key (K)** — "What information do I contain?"
- **Value (V)** — "What information do I provide?"

```
Attention(Q, K, V) = softmax(QKᵀ / √d_k) · V
```

- The dot product QKᵀ gives a similarity score (how relevant each token is to the query token)
- Dividing by √d_k (key dimension) prevents vanishing gradients from very large dot products
- Softmax converts scores to probabilities (attention weights)
- These weights are applied to V vectors to produce context-aware representations

#### Multi-Head Attention

- Runs **multiple attention mechanisms in parallel** (each "head")
- Each head attends to different aspects: one head might capture syntactic structure, another semantic relationships
- Outputs from all heads are concatenated and projected: `MultiHead = Concat(head_1, ..., head_h) · W_O`

#### Self-Attention vs Cross-Attention

- **Self-Attention** — tokens attend to other tokens in the same sequence
- **Cross-Attention** — decoder tokens attend to encoder outputs (used in seq2seq)
- **Masked Self-Attention** — each token can only attend to previous tokens (causal, used in GPT-style models)

### Modern Transformer Optimizations (Post-2017)

| Technique                         | What It Does                                                                      | Used In                    |
| --------------------------------- | --------------------------------------------------------------------------------- | -------------------------- |
| **GQA (Grouped-Query Attention)** | Groups queries to share fewer key/value heads — saves memory, speeds up inference | LLaMA 2/3, Mistral         |
| **MQA (Multi-Query Attention)**   | Extreme version of GQA — single K/V shared across all heads                       | PaLM, Falcon               |
| **Pre-Normalization (RMSNorm)**   | Normalizes before layers rather than after — more stable training at scale        | LLaMA, GPT-J               |
| **SwiGLU Activation**             | Gated linear unit — outperforms ReLU in large models                              | LLaMA, PaLM                |
| **Flash Attention**               | Memory-efficient attention using tiling — 2-4x speedup, exact same result         | LLaMA 2+, most modern LLMs |
| **Sparse Attention**              | Only attends to subset of tokens — for very long sequences                        | Longformer, Informer       |
| **KV Cache**                      | Caches past K/V computations during inference — avoids redundant computation      | All autoregressive LLMs    |

---

## Stage 7 — Large Language Models (LLMs)

### LLM Development Lifecycle

#### Phase 1 — Pre-training (Create the Base Model)

- Trained on **massive** text corpora (books, web, code, scientific papers — trillions of tokens)
- Objective: predict the next token (causal language modeling) or masked token prediction
- Learns general language, world knowledge, reasoning patterns
- Very expensive: requires thousands of GPUs for weeks/months
- Result: a **Base Model** (e.g., LLaMA 3 base, Mistral base)

#### Phase 2 — Mid-training (Domain Adaptation)

- **Domain-Specific Pre-training / Continual Pre-training** — continue training on specialized data
  - e.g., medical text (Med-PaLM), code (StarCoder), legal documents
- Injects domain knowledge without training from scratch
- Requires far fewer tokens than initial pre-training

#### Phase 3 — Post-training (Alignment & Task Tuning)

- **Supervised Fine-Tuning (SFT) / Instruction Tuning** — teach model to follow specific commands
  - Pairs of (instruction, ideal response) examples
- **RLHF (Reinforcement Learning from Human Feedback)** — align outputs with human preferences
  - Human raters rank model responses
  - Train a reward model on those rankings
  - Fine-tune LLM with PPO to maximize reward
- **DPO (Direct Preference Optimization)** — simpler alternative to RLHF, increasingly popular
- **Constitutional AI (CAI)** — Anthropic's approach using AI feedback instead of human feedback
- **Test-time Compute (Inference Scaling)** — using more computation at inference time for better reasoning (chain-of-thought, self-consistency, search)

### Fine-Tuning LLMs

#### Why Fine-Tune?

- Adapt a general model to a specific task, domain, or style
- Reduce prompt length (bake instructions into weights)
- Improve reliability and consistency

#### Full Fine-Tuning vs Parameter-Efficient Methods

- **Full Fine-Tuning** — update all model weights. Highest quality but requires massive GPU memory and time.

#### PEFT — Parameter-Efficient Fine-Tuning _(most practical for practitioners)_

| Method                         | How It Works                                                       | Use Case                            |
| ------------------------------ | ------------------------------------------------------------------ | ----------------------------------- |
| **LoRA (Low-Rank Adaptation)** | Inject small trainable low-rank matrices alongside frozen weights  | Fine-tune 7B model on a single GPU  |
| **QLoRA**                      | LoRA + quantized base model (4-bit)                                | Fine-tune 70B model on a single GPU |
| **Adapters**                   | Small bottleneck layers inserted between frozen transformer layers | Task-specific adaptation            |
| **Prefix Tuning**              | Trainable prefix tokens prepended to input                         | Prompt-level adaptation             |
| **IA³**                        | Scale activations with learned vectors                             | Very few parameters needed          |

#### Fine-Tuning Libraries

- **Unsloth** — fastest LoRA/QLoRA fine-tuning (2x+ faster than standard)
- **TRL (Transformer Reinforcement Learning)** — SFT, RLHF, DPO training by Hugging Face
- **Axolotl** — flexible fine-tuning configuration framework
- **LLaMA-Factory** — easy multi-model fine-tuning

### Working with LLM APIs (the comparatively easy side)

#### Connecting to APIs

```python
from anthropic import Anthropic

client = Anthropic()
message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Explain gradient descent."}]
)
```

- **OpenAI API** — GPT-4o, o1, o3
- **Anthropic API** — Claude family
- **Google AI** — Gemini family
- **Groq / Together AI / Fireworks** — fast inference for open models

#### Prompt Engineering

- **Zero-shot** — ask directly, no examples
- **Few-shot** — provide 2–5 examples in the prompt
- **Chain-of-Thought (CoT)** — "Let's think step by step" — improves reasoning
- **ReAct** — Reason + Act: interleave reasoning with tool use
- **System prompts** — set context, tone, constraints
- **Structured output** — JSON mode, function calling

#### Function Calling / Tool Use

- Define tools (functions) the model can invoke
- Model decides when to call a tool and with what arguments
- Foundation for building AI agents

---

## Stage 8 — Embeddings, Vector Databases & RAG

### What Are Embeddings?

- Dense numerical vectors representing meaning in high-dimensional space
- Semantically similar items have vectors close together (measured by cosine similarity)
- Used for: search, recommendations, RAG, clustering, anomaly detection

### Embedding Models

| Model                                   | Best For                         |
| --------------------------------------- | -------------------------------- |
| `text-embedding-3-small/large` (OpenAI) | General text, strong performance |
| `embed-english-v3.0` (Cohere)           | Enterprise text retrieval        |
| `BAAI/bge-m3` (open-source)             | Multilingual, high quality       |
| `nomic-embed-text` (open-source)        | Long documents                   |
| CLIP (OpenAI)                           | Joint text + image embeddings    |

### Vector Database Foundations

- **Generating embeddings** — encode documents/queries using an embedding model
- **Similarity metrics:**
  - Cosine Similarity — angle between vectors (most common)
  - Dot Product — magnitude + angle
  - Euclidean Distance — straight-line distance
- **Indexing techniques:**
  - HNSW (Hierarchical Navigable Small World) — fast approximate nearest neighbor
  - IVF (Inverted File Index) — cluster-based search
  - Flat Index — exact search, slow at scale
- **ANN (Approximate Nearest Neighbor)** — trade tiny accuracy loss for major speed gains

### Vector Databases

| Database         | Notes                                              |
| ---------------- | -------------------------------------------------- |
| **Pinecone**     | Managed, production-ready, easy to use             |
| **Weaviate**     | Open-source, built-in ML capabilities              |
| **Chroma**       | Lightweight, great for local development           |
| **Milvus**       | High-performance, enterprise scale                 |
| **Qdrant**       | Fast, Rust-based, great filtering                  |
| **pgvector**     | PostgreSQL extension — use your existing DB        |
| **FAISS** (Meta) | Library (not a DB), fastest for large-scale search |

### RAG (Retrieval-Augmented Generation)

#### Why RAG?

- LLMs have a knowledge cutoff and can hallucinate facts
- RAG grounds the LLM with retrieved real, current documents
- Much cheaper than fine-tuning for knowledge injection

#### RAG Pipeline

```
1. Document Loading     → PDF, HTML, DOCX, database rows, APIs
2. Preprocessing        → Clean, normalize, extract metadata
3. Chunking             → Split into overlapping segments
                          (fixed-size, sentence-aware, semantic chunking)
4. Embedding Generation → Encode each chunk as a vector
5. Vector Store         → Index all chunk embeddings
6. Query Time:
   User Question → Embed question → Similarity search → Retrieve top-k chunks
7. Augmentation         → Inject retrieved chunks into LLM prompt
8. Generation           → LLM generates answer grounded in retrieved context
```

#### Advanced RAG Techniques

- **Hybrid Search** — combine dense (vector) + sparse (BM25 keyword) retrieval
- **Reranking** — use a cross-encoder to re-score retrieved chunks (Cohere Rerank, BGE Reranker)
- **HyDE (Hypothetical Document Embeddings)** — generate a hypothetical answer, embed it, then search
- **Multi-query retrieval** — rephrase query multiple ways, combine results
- **Parent-child chunking** — retrieve small chunks, return their larger parent context

#### RAG Evaluation

- **RAGAS** — metrics: faithfulness, answer relevancy, context precision/recall
- **DeepEval** — comprehensive LLM evaluation framework
- **TruLens** — tracing and evaluation

#### RAG Frameworks

- **LangChain** — most popular, large ecosystem
- **LlamaIndex** — specialized in data ingestion and indexing
- **Haystack** — production-focused NLP pipelines

---

## Stage 9 — AI Agents

### What Is an AI Agent?

An AI agent is a system that uses an LLM as its "brain" to autonomously decide which actions to take, execute them, observe results, and repeat until a goal is achieved.

```
User Goal → LLM (brain) → Plan → Choose Tool → Execute → Observe Result → Loop
```

### Core Concepts

#### Agent Fundamentals

- The agent receives a goal and iteratively decides on actions
- Loop: `Think → Act → Observe → Think again`
- Common frameworks: ReAct (Reason + Act), CoT + Tool Use

#### Tool Use / Function Calling

- Agents extend their capabilities by calling external tools
- Common tools: web search, code execution, calculator, database queries, file read/write, APIs
- The LLM outputs structured JSON describing the tool and arguments — the framework executes it

#### Planning

- **Task decomposition** — break a complex task into subtasks
- **Chain-of-Thought** — reason through each step
- **Tree of Thoughts (ToT)** — explore multiple reasoning paths
- **ReAct** — interleave reasoning (Thought) with actions (Act) and observations

#### Memory

| Memory Type                 | Description                                                  |
| --------------------------- | ------------------------------------------------------------ |
| **Short-term (in-context)** | Conversation history in the prompt window                    |
| **Long-term (external)**    | Store and retrieve from a vector database or key-value store |
| **Episodic**                | Recall specific past interactions                            |
| **Semantic**                | Facts and domain knowledge stored as embeddings              |

#### Multi-Agent Systems

- Multiple specialized agents working together
- **Orchestrator agent** — plans and delegates to specialist agents
- **Specialist agents** — each handles a specific domain (e.g., a researcher agent + a writer agent + a fact-checker agent)
- Enables complex workflows that exceed a single agent's context window

### Key Agent Frameworks

| Framework                     | Key Feature                                                   |
| ----------------------------- | ------------------------------------------------------------- |
| **LangGraph**                 | Stateful multi-agent graphs with cycles — built on LangChain  |
| **AutoGen** (Microsoft)       | Conversational multi-agent framework                          |
| **CrewAI**                    | Role-based multi-agent collaboration — simpler than LangGraph |
| **CAMEL**                     | Role-playing agents (user + assistant) for task-solving       |
| **Smolagents** (Hugging Face) | Lightweight, open-source agent framework                      |
| **LangChain Agents**          | Built-in agent executors with large tool ecosystem            |

---

## Stage 10 — Model Context Protocol (MCP)

### What Is MCP?

- MCP (Model Context Protocol) is an **open standard** by Anthropic for connecting AI agents to external data sources and tools
- Think of it as "USB-C for AI" — a universal interface
- Replaces ad-hoc custom integrations with a standardized protocol

### Core Functions

- **Tool connectivity** — expose any function as a tool an agent can call
- **Resource access** — provide agents with access to files, databases, APIs
- **OAuth / Authorization management** — secure, scoped access to external services
- **Database access** — query structured data without custom connectors
- **API integration** — connect to any REST or GraphQL API
- **Code execution** — run code sandboxes, return results

### MCP Architecture

```
AI Agent (Claude, GPT, etc.)
      ↓ MCP Protocol
MCP Server
      ↓
External Tools / Data
(GitHub, Google Drive, Databases, Custom APIs, File Systems)
```

- **MCP Client** — the AI model host (e.g., Claude Desktop)
- **MCP Server** — exposes tools/resources as MCP endpoints
- **Transport** — local (stdio), remote (SSE over HTTP)

### Infrastructure (MLOps Context)

- **MLOps Paradigms** — CI/CD for models, reproducibility, monitoring
- **Experiment tracking** — MLflow, W&B
- **Docker** — containerize agents and inference servers
- **Kubernetes** — orchestrate agent workloads at scale

### Inference Optimization

- **TensorRT** — NVIDIA's inference optimizer (up to 8x speedup on GPU)
- **ONNX / ONNX Runtime** — cross-platform inference
- **vLLM** — high-throughput LLM serving with PagedAttention
- **llama.cpp** — CPU/GPU inference for LLMs, quantization support
- **Quantization** — INT8, INT4 (4-bit) — shrink model size, faster inference

---

## Stage 11 — MLOps & Deployment

### Model Packaging & Serving

- Serialization: Pickle, Joblib, ONNX
- REST APIs: **FastAPI** (recommended), Flask
- gRPC for high-performance inference
- Model serving: TorchServe, TensorFlow Serving, BentoML, Ray Serve, **vLLM** (for LLMs)

### Containerization & Orchestration

- **Docker** — containerize your model API
- **Kubernetes** — scale containers in production
- **Helm** — Kubernetes package management

### Cloud Platforms

| Cloud        | ML Service          |
| ------------ | ------------------- |
| AWS          | SageMaker           |
| Google Cloud | Vertex AI           |
| Azure        | Azure ML            |
| Open-source  | MLflow + Kubernetes |

### Edge Deployment

- TensorFlow Lite (mobile/IoT)
- ONNX Runtime
- Core ML (Apple devices)
- OpenVINO (Intel hardware)
- Quantization & Pruning

### Experiment Tracking

- **MLflow** — open source, self-hosted
- **Weights & Biases (W&B)** — industry standard
- **ClearML, Neptune.ai** — alternatives

### CI/CD for ML

- GitHub Actions / GitLab CI for automated testing
- Automated model retraining pipelines
- Shadow deployment — run new model in parallel before cutover
- A/B testing models in production
- Tools: **ZenML**, Kubeflow, Metaflow (Netflix), Argo Workflows

### Monitoring & Observability

- **Data Drift** — input feature distributions change
- **Concept Drift** — relationship between X and Y changes
- **Label Drift** — output distribution shifts
- Tools: **Evidently AI**, WhyLabs, Arize AI
- Logging: Prometheus + Grafana, Datadog

### Model Interpretability

- **SHAP** (SHapley Additive exPlanations) — explains any model
- **LIME** — Local Interpretable Model-Agnostic Explanations
- **Grad-CAM** — visualizes CNN attention on images
- **Feature Importance** (tree models), Partial Dependence Plots

---

## Stage 12 — Real-World Considerations

### Ethics & Fairness

- Bias sources: data bias, labeling bias, historical bias, feedback loops
- Fairness metrics: demographic parity, equal opportunity, individual fairness
- Tools: Fairlearn (Microsoft), AI Fairness 360 (IBM)
- Document your models: model cards, datasheets for datasets

### Data Privacy & Security

- GDPR, HIPAA compliance for ML systems
- **Differential Privacy** — add mathematical noise to protect individual records
- **Federated Learning** — train on-device, never share raw data (Google Gboard)
- Adversarial examples, model inversion attacks, membership inference
- PII detection and redaction before training

### Production Performance

- Latency vs throughput tradeoffs
- Quantization (INT8, FP16) — 4x speedup with minimal loss
- Knowledge Distillation — train a small model to mimic a large one
- TensorRT, ONNX Runtime, vLLM for inference optimization

### Scalability

- Distributed training: PyTorch DDP (Data Distributed Parallel)
- **DeepSpeed, FSDP (Fully Sharded Data Parallel)** — training models too large for one GPU
- Data parallelism vs Model parallelism vs Pipeline parallelism

---

## Stage 13 — Staying Current

> The field moves fast. Staying current is not optional — it's a job requirement.

### Where to Follow Research

| Resource                          | What It Gives You                      |
| --------------------------------- | -------------------------------------- |
| **arXiv (cs.LG, cs.AI, cs.CL)**   | Pre-print papers before peer review    |
| **Papers With Code**              | Papers + implementations + benchmarks  |
| **Hugging Face Blog**             | New models, datasets, practical guides |
| **Google DeepMind / OpenAI Blog** | Announcements, technical reports       |
| **Andrej Karpathy (YouTube/X)**   | Deep, practical ML intuition           |
| **Kaggle**                        | Competitions, notebooks, real datasets |

### Practical Strategies

- **Always keep on learning new things** — dedicate time each week to one new paper or concept
- **Build things** — reading without building leads to shallow understanding
- **Rapid development — adapt fast** — prototype in days, not months
- Compete on Kaggle to sharpen real skills under constraints
- Contribute to open-source (Hugging Face, PyTorch ecosystem)
- Write about what you learn — blog posts cement understanding

### Learning Roadmap by Level

#### Beginner (0–3 months)

1. Python basics + Pandas + NumPy + SQL fundamentals
2. Math: Linear Algebra + Probability basics
3. Scikit-Learn: regression + classification on tabular data
4. First project: House price prediction or Titanic survival (Kaggle)

#### Intermediate (3–9 months)

1. Deep Learning with PyTorch (MLP, CNN, backprop)
2. Hugging Face — fine-tune a pre-trained BERT or GPT model
3. Build a RAG application with LangChain + Chroma
4. MLflow for experiment tracking
5. Full pipeline: data → model → FastAPI → Docker

#### Advanced (9+ months)

1. Specialize: NLP/LLMs, CV, RL, or Generative AI
2. MLOps: CI/CD, drift monitoring, A/B testing
3. LLM Engineering: fine-tuning with QLoRA, MCP, multi-agent systems
4. Read and implement papers from arXiv
5. Contribute to open-source

---

## The Complete Iterative Workflow

```
1. DEFINE     → Business problem, success metric, constraints
2. COLLECT    → Data sources (SQL!), labeling, quality checks
3. PROCESS    → Clean, engineer features, split data
4. TRAIN      → Baseline first, then improve iteratively
5. EVALUATE   → Metrics, error analysis, fairness check
6. EXPLAIN    → SHAP/LIME — understand model decisions
7. DEPLOY     → Containerize, API, CI/CD pipeline
8. MONITOR    → Drift detection, performance dashboards
9. RETRAIN    → Triggered by drift or scheduled — loop back to step 2
```

---

## What This Roadmap Added (vs Your Original Notes)

| New Addition                               | Why It Matters                                    |
| ------------------------------------------ | ------------------------------------------------- |
| **Full SQL Roadmap (7 levels)**            | SQL is the #1 skill interviewers test before ML   |
| Python fundamentals section                | Explicit foundation before ML libraries           |
| Optimization theory (Adam, warmup)         | You can't tune LLMs without this                  |
| MLP + backprop deep dive with code         | Understanding beats copying                       |
| SwiGLU, RoPE, GQA, Flash Attention         | What modern LLMs actually use                     |
| Full LLM lifecycle (pre/mid/post-training) | Understanding GPT/LLaMA architecture deeply       |
| Fine-tuning: LoRA, QLoRA, Unsloth, TRL     | The practical fine-tuning toolkit                 |
| RAG pipeline + advanced techniques         | Most in-demand production LLM skill               |
| AI Agents: LangGraph, CrewAI, CAMEL        | The next wave of AI applications                  |
| MCP (Model Context Protocol)               | The emerging standard for agent-tool connectivity |
| Speech & audio processing                  | Complete the "paths" section                      |
| GNNs                                       | Fraud, molecules, recommendations                 |
| Ethics, fairness, privacy                  | Required in enterprise AI                         |
| Staying current: arXiv, Papers With Code   | How top engineers stay sharp                      |

---

_Last updated: 2025 | This is a living document — the field evolves continuously. Always cross-reference with the latest documentation and papers._
