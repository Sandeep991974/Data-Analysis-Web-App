import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# Title and Subheader
st.title("---📊 Data Analysis App---")
st.subheader("Analyze your CSV file data here")
st.subheader("Data Analysis Using 🐍 Python libraries - Streamlit, Pandas, Seaborn ,Matplotlib")

# Upload Dataset
upload = st.file_uploader(" 📁Upload your dataset (in csv format)")
if upload is not None:
    data = pd.read_csv(upload)

# Show Dataset
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())    


# check DataType of each columns

if upload is not None:
    if st.checkbox("DataTypes of Each Column"):
        st.text("DataType")
        st.write(data.dtypes)

#  Find the shape of our Dataset (number of row and number of column)

if upload is not None:
    data_shape =  st.radio("❓What dimension do you want to check ?",('Rows','Columns'))
    if data_shape=='Rows':
        st.write("Number of Rows :",data.shape[0])
    else:    
        st.write("Number of Columns :",data.shape[1])


# Find the null values in the dataset
if upload is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox("Null Values in the Dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("🎉 Congratulations !! , No missing value in dataset.")  



# Find Duplicate values in Dataset
# Missing values Handling

if upload is not None:
    if data.isnull().sum().sum()>0:
        st.subheader("🖌️ Handle Missing Values")
        missing_data = data.isnull().sum()

        missing_data = missing_data[missing_data>0]

        st.write("### Missing Values by Column")
        st.dataframe(missing_data)

        option = st.selectbox(
            "How to you want to handle missing values?",
            [
                "Selection an option",
                "Drop rows",
                "Fill with Mean",
                "Fill with Median",
                "Fill with Mode"
            ]
        )
        if option =="Drop rows":
            data = data.dropna()
            st.success("✅ Rows containing missing values have been removed.")
        elif option=='Fill with Mean':
            numeric_column = data.select_dtypes(include="number").columns
            data[numeric_column] = data[numeric_column].fillna(data[numeric_column].mean())  
            st.success("✅ Missing Numerical Values filled with Mean.")
        elif option=='Fill with Median':
            numeric_column = data.select_dtypes(include="number").columns
            data[numeric_column] = data[numeric_column].fillna(data[numeric_column].median())  
            st.success("✅ Missing Numerical Values filled with Median.")
        elif option == "Fill with Mode":
            for column in data.columns :
                if data.isnull().any():
                    data[column] = data[column].fillna(data[column].mode()[0])   
                    st.success("✅ Missing values filled with Mode.")
        else:
            st.success("🎉 No missing values found in the dataset.")

# Delete Unwanted Columns

if upload is not None:

    st.subheader("🗑️ Remove Unwanted Columns")

    columns_to_remove = st.multiselect(
        "Select columns you want to remove:",
        data.columns
    )

    if st.button("Remove Selected Columns"):

        if columns_to_remove:
            data = data.drop(columns=columns_to_remove)

            st.success(
                f"✅ Removed {len(columns_to_remove)} column(s)."
            )

            st.dataframe(data.head())

        else:
            st.warning("⚠️ Please select at least one column.")

# Rename Column

if upload is not None:

    st.subheader("✏️ Rename Column")

    column_to_rename = st.selectbox(
        "Select column:",
        data.columns
    )

    new_name = st.text_input(
        "Enter new column name:"
    )

    if st.button("Rename Column"):

        if new_name.strip():

            data = data.rename(
                columns={column_to_rename: new_name}
            )

            st.success(
                f"✅ '{column_to_rename}' renamed to '{new_name}'."
            )

        else:
            st.warning("⚠️ Enter a valid column name.")

# Change Data Type

if upload is not None:

    st.subheader("🔄 Change Data Type")

    column = st.selectbox(
        "Select column:",
        data.columns,
        key="datatype_column"
    )

    new_dtype = st.selectbox(
        "Select new data type:",
        ["string", "integer", "float"]
    )

    if st.button("Change Data Type"):

        try:

            if new_dtype == "string":
                data[column] = data[column].astype(str)

            elif new_dtype == "integer":
                data[column] = pd.to_numeric(
                    data[column]
                ).astype("Int64")

            elif new_dtype == "float":
                data[column] = pd.to_numeric(
                    data[column]
                ).astype(float)

            st.success(
                f"✅ '{column}' converted to {new_dtype}."
            )

        except Exception:
            st.error(
                "❌ This column cannot be converted to the selected type."
            )

# Exploratory Data Analysis (EDA)

if upload is not None:

    st.header("📊 Exploratory Data Analysis")

    analysis_type = st.selectbox(
        "Select Analysis Type",
        [
            "Select One",
            "Value Counts",
            "Sorting",
            "Filtering",
            "Group By",
            "Column Statistics"
        ]
    )
    # 1. VALUE COUNTS
    
    if analysis_type == "Value Counts":

        st.subheader("🔢 Value Counts")

        column = st.selectbox(
            "Select a column:",
            data.columns,
            key="value_counts_column"
        )

        result = data[column].value_counts()

        st.dataframe(result)

        # Optional chart
        if st.checkbox("📊 Show Value Count Chart"):

            st.bar_chart(result)
   
    # 2. SORTING

    elif analysis_type == "Sorting":

        st.subheader("↕️ Sort Dataset")

        column = st.selectbox(
            "Select column to sort:",
            data.columns,
            key="sorting_column"
        )

        order = st.radio(
            "Select sorting order:",
            ["Ascending", "Descending"]
        )

        if st.button("Sort Data"):

            if order == "Ascending":
                sorted_data = data.sort_values(
                    by=column,
                    ascending=True
                )
            else:
                sorted_data = data.sort_values(
                    by=column,
                    ascending=False
                )

            st.dataframe(sorted_data)

    # 3. FILTERING
    

    elif analysis_type == "Filtering":

        st.subheader("🔎 Filter Dataset")

        column = st.selectbox(
            "Select column:",
            data.columns,
            key="filter_column"
        )

        # Numerical column
        if pd.api.types.is_numeric_dtype(data[column]):

            min_value = float(data[column].min())
            max_value = float(data[column].max())

            selected_range = st.slider(
                "Select value range:",
                min_value,
                max_value,
                (min_value, max_value)
            )

            filtered_data = data[
                (data[column] >= selected_range[0]) &
                (data[column] <= selected_range[1])
            ]

            st.write(
                f"Rows found: {len(filtered_data)}"
            )

            st.dataframe(filtered_data)

        # Categorical column
        else:

            values = data[column].dropna().unique()

            selected_values = st.multiselect(
                "Select values:",
                values
            )

            if selected_values:

                filtered_data = data[
                    data[column].isin(selected_values)
                ]

                st.write(
                    f"Rows found: {len(filtered_data)}"
                )

                st.dataframe(filtered_data)

            else:

                st.info(
                    "Select at least one value to filter."
                )

    # 4. GROUP BY

    elif analysis_type == "Group By":

        st.subheader("📊 Group By Analysis")

        group_column = st.selectbox(
            "Select grouping column:",
            data.columns,
            key="group_column"
        )

        numeric_columns = data.select_dtypes(
            include="number"
        ).columns

        if len(numeric_columns) > 0:

            value_column = st.selectbox(
                "Select numerical column:",
                numeric_columns,
                key="group_value_column"
            )

            operation = st.selectbox(
                "Select operation:",
                [
                    "Sum",
                    "Mean",
                    "Median",
                    "Minimum",
                    "Maximum",
                    "Count"
                ]
            )

            if st.button("Perform Group By"):

                if operation == "Sum":

                    result = data.groupby(
                        group_column
                    )[value_column].sum()

                elif operation == "Mean":

                    result = data.groupby(
                        group_column
                    )[value_column].mean()

                elif operation == "Median":

                    result = data.groupby(
                        group_column
                    )[value_column].median()

                elif operation == "Minimum":

                    result = data.groupby(
                        group_column
                    )[value_column].min()

                elif operation == "Maximum":

                    result = data.groupby(
                        group_column
                    )[value_column].max()

                else:

                    result = data.groupby(
                        group_column
                    )[value_column].count()

                st.dataframe(result)


        else:

            st.warning(
                "⚠️ No numerical columns available for Group By analysis."
            )

    # 5. COLUMN STATISTICS

    elif analysis_type == "Column Statistics":

        st.subheader("📈 Column Statistics")

        numeric_columns = data.select_dtypes(
            include="number"
        ).columns

        if len(numeric_columns) > 0:

            column = st.selectbox(
                "Select numerical column:",
                numeric_columns,
                key="statistics_column"
            )

            col1, col2, col3 = st.columns(3)
            col4, col5, col6 = st.columns(3)

            col1.metric(
                "Count",
                data[column].count()
            )

            col2.metric(
                "Mean",
                round(data[column].mean(), 2)
            )

            col3.metric(
                "Median",
                round(data[column].median(), 2)
            )

            col4.metric(
                "Minimum",
                data[column].min()
            )

            col5.metric(
                "Maximum",
                data[column].max()
            )

            col6.metric(
                "Standard Deviation",
                round(data[column].std(), 2)
            )

        else:

            st.warning(
                "⚠️ No numerical columns available."
            )

# DASHBOARD

if upload is not None:

    st.header("🎯 Dataset Dashboard")

    # Dataset Metrics
    total_rows = data.shape[0]
    total_columns = data.shape[1]
    total_missing = data.isnull().sum().sum()
    total_duplicates = data.duplicated().sum()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📌 Total Rows",
        total_rows
    )

    col2.metric(
        "📋 Total Columns",
        total_columns
    )

    col3.metric(
        "❌ Missing Values",
        total_missing
    )

    col4.metric(
        "♻️ Duplicate Rows",
        total_duplicates
    )

    st.divider()

    # Dataset Information
    st.subheader("📋 Dataset Information")

    col1, col2 = st.columns(2)

    with col1:

        st.write("### 📊 Numerical Columns")

        numerical_columns = data.select_dtypes(
            include="number"
        ).columns

        if len(numerical_columns) > 0:
            st.write(
                list(numerical_columns)
            )
        else:
            st.info("No numerical columns found.")

    with col2:

        st.write("### 🔤 Categorical Columns")

        categorical_columns = data.select_dtypes(
            exclude="number"
        ).columns

        if len(categorical_columns) > 0:
            st.write(
                list(categorical_columns)
            )
        else:
            st.info("No categorical columns found.")

    st.divider()

    # Statistical Summary
    st.subheader("📈 Numerical Summary")

    numeric_data = data.select_dtypes(
        include="number"
    )

    if not numeric_data.empty:

        summary = numeric_data.describe().T

        summary = summary[
            [
                "count",
                "mean",
                "min",
                "max"
            ]
        ]

        summary.columns = [
            "Count",
            "Mean",
            "Minimum",
            "Maximum"
        ]

        st.dataframe(
            summary,
            width="stretch"
        )

    else:

        st.info(
            "No numerical data available for summary."
        )



# EXPORT / DOWNLOAD DATA

if upload is not None:

    st.header("💾 Export Dataset")

    st.write(
        "Download your current dataset after analysis and cleaning."
    )

    # Convert DataFrame to CSV
    csv_data = data.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download Dataset as CSV",
        data=csv_data,
        file_name="cleaned_dataset.csv",
        mime="text/csv"
    )

# Get Overall Statistics
if upload is not None:
    if st.checkbox("Summary of the Dataset"):
        st.write(data.describe(include='all'))



# About Section
if st.button("About App"):
    st.header("---Data Analysis Web App---")
    st.text("This is a Data Analysis Web App, where you can do all basic opertaions related to the data analysis like- Data preview, DataTyes of each columns, No.of Rows and Columns, Checking Missing values and drop the missing values if you want, Summary of Dataset.")
    st.text("Built with Streamlit")        

# By         

if st.checkbox("🙋 By"):
  st.success("---Made by Sandeep Chaurasiya---")   
