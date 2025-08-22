import streamlit as st
import json
import pandas as pd

def extract_usernames(data, key=None):
    if isinstance(data, dict) and key:
        entries = data.get(key, [])
    elif isinstance(data, list):
        entries = data
    else:
        entries = []

    usernames = set()
    for entry in entries:
        if "string_list_data" in entry:
            for item in entry["string_list_data"]:
                if "value" in item:
                    usernames.add(item["value"])
    return usernames

st.set_page_config(page_title="Instagram Followers Checker", page_icon="📱", layout="wide")

st.title("📱 Instagram Followers Checker")
st.markdown("Upload your `followers.json` and `following.json` files to see who follows you back and who doesn’t.")

st.markdown("""
### ℹ️ How to get your Instagram data

To use this tool, you first need to **download your Instagram data**:

1. Go to 👉 [Instagram Data Download](https://www.instagram.com/download/request/)  
2. Log in with your Instagram account.  
3. Request **connections data**, not necessary all data. Select **followers and following**.
4. ⚠️ Make sure to select the format **JSON** (not HTML).  
5. When Instagram sends you the files, look for:
   - `followers_1.json`
   - `following.json`

Upload those files here to see who follows you back and who doesn’t.
""")

followers_file = st.file_uploader("📂 Upload followers.json", type="json")
following_file = st.file_uploader("📂 Upload following.json", type="json")

if followers_file and following_file:
    followers_data = json.load(followers_file)
    following_data = json.load(following_file)

    followers = extract_usernames(followers_data)
    following = extract_usernames(following_data, "relationships_following")

    not_following_back = sorted(following - followers)
    not_followed_by_me = sorted(followers - following)

    st.markdown("---")
    st.header("🔍 Results")

    # --- Accounts you follow that don't follow you back ---
    st.subheader("❌ Accounts you follow that do NOT follow you back")
    if not_following_back:
        st.error(f"{len(not_following_back)} accounts found")
        df_not_following_back = pd.DataFrame(not_following_back, columns=["Username"])
        st.dataframe(df_not_following_back, use_container_width=True)
    else:
        st.success("✅ Everyone you follow also follows you back!")

    # --- Accounts that follow you but you don't follow back ---
    st.subheader("⚠️ Accounts that follow you but you do NOT follow back")
    if not_followed_by_me:
        st.warning(f"{len(not_followed_by_me)} accounts found")
        df_not_followed_by_me = pd.DataFrame(not_followed_by_me, columns=["Username"])
        st.dataframe(df_not_followed_by_me, use_container_width=True)
    else:
        st.success("✅ You follow everyone who follows you!")

    # --- Download results as TXT ---
    results_txt = "\n".join([
        "Accounts you follow that do NOT follow you back:",
        *not_following_back,
        "",
        "Accounts that follow you but you do NOT follow back:",
        *not_followed_by_me
    ])

    st.download_button(
        "📥 Download results as TXT",
        data=results_txt,
        file_name="instagram_results.txt"
    )
