
## Code Explanation

- *Import libraries*:  
We import pandas for data handling and streamlit to create the web app.

- *Load dataset*:  
We load the sales CSV data directly from the provided GitHub Gist URL using pandas.read_csv().

- *Display data*:  
The app shows the first 5 rows of the dataset using st.dataframe().

- *User interaction*:  
The app provides two select boxes:
- One to choose the chart type (Line or Bar).
- Another to select the column from the dataset to visualize.

- *Display chart*:  
Based on the user’s choice, the app renders either a line chart or bar chart using st.line_chart() or st.bar_chart().

---

## Git Commands Used

```bash
git init
git add .
git commit -m "Initial commit - Streamlit sales app"
git remote add origin https://gi…
[4:21 am, 15/07/2025] mariam🤍: Week 1 - Sales Data Visualization with Streamlit

This project is a basic interactive Streamlit web application that visualizes a company's sales data using pandas and Streamlit charts.

تم بناء هذا التطبيق البسيط باستخدام مكتبة Streamlit لعرض بيانات مبيعات شركة باستخدام الرسوم البيانية، ويوفر خيارات تفاعلية للمستخدم لاختيار نوع الرسم البياني والعمود.

---

## Git Commands Used

1. git init  
   Initialize a local Git repository.  
   تهيئة مستودع Git جديد على جهازي المحلي.

2. git add .  
   Add all files to the staging area.  
   إضافة كل الملفات الجديدة للتتبع.

3. git commit -m "Initial commit"  
   Save a snapshot of the project with a message.  
   حفظ التعديلات برسالة توضح التغيير.

4. git remote add origin <repo-url>  
   Link the local repo with GitHub.  
   ربط المستودع المحلي بحساب GitHub.

5. git push -u origin main  
   Upload files to GitHub repository.  
   رفع الملفات على المستودع على GitHub.

---

## Code Explanation

python
import streamlit as st
import pandas as pd


> Importing required libraries.  
> استيراد المكتبات اللازمة: Streamlit و pandas.

python
url = "https://gist.githubusercontent.com/kevin336/acbb2271e66c18a5b73aacf82ca82784/raw/company-sales.csv"
df = pd.read_csv(url)


> Load data from the provided GitHub Gist CSV file using pandas.  
> تحميل بيانات المبيعات من الرابط باستخدام read_csv.

python
st.title("Company Sales")


> Display the title of the app.  
> عرض عنوان التطبيق على الواجهة.

python
st.write("### Display first 5 rows:")
st.dataframe(df.head())


> Show a preview of the dataset.  
> عرض أول خمس صفوف من البيانات.

python
chart_type = st.selectbox("Select chart type:", ["Line", "Bar"])
column = st.selectbox("Select column:", df.columns[1:])


> Create two dropdowns: one for chart type, one for selecting a column.  
> إنشاء خيارات لاختيار نوع الرسم البياني والعمود الذي سيتم رسمه.

python
st.write("### Chart:")
if chart_type == "Line":
    st.line_chart(df[column])
else:
    st.bar_chart(df[column])


> Display the selected chart based on user input.  
> عرض الرسم البياني بناءً على الاختيارات.

---

## How to Run This Project

1. Open terminal.
2. Activate virtual environment (if needed).
3. Install dependencies:
   bash
   pip install streamlit pandas
   
4. Run the app:
   bash
   streamlit run app.py
   

> سيتم فتح المتصفح تلقائيًا لتشغيل التطبيق.

---

## Resources Used

- Streamlit Docs: https://docs.streamlit.io/
- Pandas Docs: https://pandas.pydata.org/docs/
- Git & GitHub (Elzero Arabic): https://www.youtube.com/playlist?list=PLDoPjvoNmBAw4eOj58MZPakHjaO3frVMF

---

## Author

- Name: Mariam Mohammed  
- Repository: https://github.com/mariammohammed2/Week1-MariamMohammed