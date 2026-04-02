<div align="center">

<img src="Glamora_Preview.jpeg" alt="Glamora Banner" width="100%" style="border-radius: 12px;" />

# ✨ Glamora
### AI-Powered Fashion Recommender Assistant

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.x-092E20?style=flat-square&logo=django&logoColor=white)](https://djangoproject.com)
[![React](https://img.shields.io/badge/React-18.x-61DAFB?style=flat-square&logo=react&logoColor=black)](https://react.dev)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-ML-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

**Full-stack intelligent fashion eCommerce platform** that learns your style, clusters users by taste, and delivers hyper-relevant product recommendations — powered by NLP, k-means clustering, and cosine similarity.

[🎬 Watch Demo](https://youtu.be/VxpacFwaPFY) · [📂 GitHub](https://github.com/zeeshanibrarali/Glamora) · [🌐 Live Portfolio](https://zinov.pythonanywhere.com)

</div>

---

## 🧠 What Makes Glamora Different

Glamora isn't just another online store. It's an **intelligent fashion advisor** built with a hybrid ML recommendation engine that combines content-based filtering and collaborative clustering to serve each user highly personalized product suggestions — achieving **89% relevance accuracy** across 1,000+ user profiles.

```
quiz_input → NLP (TF-IDF) → user_vector → k-means cluster → cosine_sim (products in cluster) → top 5 products
```

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                        Glamora                          │
│                                                         │
│  ┌──────────┐    ┌──────────────┐    ┌───────────────┐  │
│  │  React   │◄──►│  Django REST │◄──►│  ML Engine    │  │
│  │ Frontend │    │   Backend    │    │  (Scikit +    │  │
│  └──────────┘    └──────────────┘    │   TF-IDF +    │  │
│                        │             │   k-means)    │  │
│                  ┌─────▼──────┐      └───────────────┘  │
│                  │ PostgreSQL │                          │
│                  │   / DB     │                          │
│                  └────────────┘                          │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 Features

### 🛍️ eCommerce Core
- **User Authentication** — Secure registration, login, password reset, and profile management
- **Product Catalog** — Rich product browsing with search, filters, and detailed descriptions
- **Shopping Cart** — Add, update, and remove items seamlessly
- **Checkout Flow** — Smooth order summary, address management, and Razorpay payment integration
- **Order Management** — Full order history and real-time status tracking
- **Admin Panel** — Django admin for managing products, orders, and users
- **Responsive UI** — Mobile-first design using Bootstrap

### 🤖 AI / ML Recommendation Engine
| Component | Implementation |
|-----------|---------------|
| **Style Profiling** | Onboarding quiz captures user preferences |
| **NLP Vectorization** | TF-IDF transforms style keywords into user vectors |
| **Smart Clustering** | K-Means groups users by fashion taste |
| **Similarity Matching** | Cosine similarity ranks products within a cluster |
| **Output** | Top 5 hyper-relevant product recommendations |

**Relevance Accuracy: 89%** | **Scalability: 1,000+ user profiles**

---

## 🛠️ Tech Stack

| Layer | Technologies |
|-------|-------------|
| **Frontend** | React, Bootstrap, HTML/CSS/JavaScript |
| **Backend** | Django, Django REST Framework |
| **ML / AI** | Scikit-learn (TF-IDF, k-means, cosine similarity), Pandas, NumPy |
| **Database** | PostgreSQL |
| **Payments** | Razorpay API |
| **Dev Tools** | Jupyter Notebook, Google Colab, GitHub |

---

## 📦 Setup & Installation

### Prerequisites
- Python 3.10+
- Node.js 18+
- PostgreSQL

### 1. Clone the Repository
```bash
git clone https://github.com/zeeshanibrarali/Glamora.git
cd Glamora
```

### 2. Backend Setup
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
# .\venv\Scripts\activate       # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:
```env
SECRET_KEY=your_secret_key_here
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/glamora
RAZORPAY_KEY_ID=your_razorpay_key
RAZORPAY_KEY_SECRET=your_razorpay_secret
```

> **Generate a Django secret key:**
> ```bash
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

### 4. Apply Migrations & Create Superuser
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Frontend Setup
```bash
cd frontend
npm install
npm start
```

### 6. Run the Development Server
```bash
# In the root directory
python manage.py runserver
```

Navigate to **http://127.0.0.1:8000** 🎉

---

## 🔗 Usage

| URL | Description |
|-----|-------------|
| `http://127.0.0.1:8000/` | Main storefront |
| `http://127.0.0.1:8000/admin/` | Django admin panel |
| `http://127.0.0.1:8000/api/recommendations/` | AI recommendation endpoint |

---

## 📊 ML Performance Summary

```
Hybrid Recommendation Engine
─────────────────────────────
Relevance Accuracy     : 89%
User Profiles Scaled   : 1,000+
Clustering Algorithm   : K-Means (content + collaborative hybrid)
Vectorization          : TF-IDF on style keywords
Similarity Metric      : Cosine Similarity
```

---

## 📁 Project Structure

```
Glamora/
├── backend/
│   ├── glamora/              # Django project settings
│   ├── products/             # Product catalog app
│   ├── users/                # Authentication & profiles
│   ├── orders/               # Cart & order management
│   ├── recommendations/      # ML engine (TF-IDF, k-means, cosine)
│   └── payments/             # Razorpay integration
├── frontend/
│   ├── src/
│   │   ├── components/       # React UI components
│   │   ├── pages/            # Route-level pages
│   │   └── services/         # API calls
│   └── public/
├── ml_notebooks/             # Jupyter notebooks for model training
├── requirements.txt
├── .env.example
└── manage.py
```

---

## 🤝 Contributing

Contributions are welcome! To get started:

1. Fork this repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'feat: add your feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please follow [conventional commits](https://www.conventionalcommits.org/) and ensure your code is clean and tested.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Zeeshan Ibrar** — Python AI/ML Developer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/zeeshan-ibrar-6a3913256/)
[![YouTube](https://img.shields.io/badge/YouTube-Channel-FF0000?style=flat-square&logo=youtube)](https://www.youtube.com/channel/UClUyQ6LbQAUR0UZ0BUTF9ow)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-1a1a2e?style=flat-square&logo=globe)](https://zinov.pythonanywhere.com)
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?style=flat-square&logo=gmail)](mailto:inboxtozeeshanibrar@gmail.com)

---

<div align="center">
  <sub>Built with ❤️ using Django, React, and Machine Learning</sub>
</div>
