# Instagram Followers Checker

A simple **Streamlit app** that helps you check who **follows you back** on Instagram and who doesn’t.  
It uses the official **Instagram Data Download** (JSON format) to analyze your **followers** and **following** lists.  

---

## Features

- See which accounts you follow that don’t follow you back  
- See which accounts follow you but you don’t follow back  
- Interactive tables with search and sorting  
- Export results as a `.txt` file  
- Clean and modern interface with Streamlit  

---

## How to get your Instagram data

1. Go to 👉 [Instagram Data Download](https://www.instagram.com/download/request/)  
2. Log in with your Instagram account  
3. Request **a copy of your connections data**  
4. ⚠️ Make sure to select **JSON format** (not HTML)  
5. After receiving your data, locate these two files:
   - `followers_1.json`  
   - `following.json`  

---

## How to run the app

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/instagram-followers-checker.git
cd instagram-followers-checker
```

### 2. Install dependencies
It is recommended to use pipx or a virtual environment. For example:
```bash
pip install streamlit pandas
```

### 3. Run the app

```bash
streamlit run instagram-connections.py
```

### 4. Upload your JSON files

- Upload `followers.json`
- Upload `following.json`

Enjoy the results! 🎉
