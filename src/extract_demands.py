import pyodbc
import pandas as pd

def load_data_from_mdb(file_path, table_name):
    """Load data from an .mdb file."""
    conn_str = (
        f"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};"
        f"DBQ={file_path};"
    )
    conn = pyodbc.connect(conn_str)
    query = f"SELECT * FROM {table_name}"
    data = pd.read_sql(query, conn)
    conn.close()
    return data


def calculate_average_demand(data):
    """Calculate the average demand for each product for month 2, and multiply by 2."""
    # Filter data for month 2
    month_2_data = data[data['Month'] == 2]

    # Group by product and calculate the average demand
    average_demand = month_2_data.groupby('Product_Num')['Demand'].mean().reset_index()

    # Multiply average demand by 2
    average_demand['Average_Demand'] = average_demand['Demand'] * 2
    average_demand.rename(columns={'Demand': 'Average_Demand'}, inplace=True)

    return average_demand


def save_to_mdb(dataframe, file_path, table_name):
    """Save the DataFrame to a table in an .mdb file."""
    conn_str = (
        f"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};"
        f"DBQ={file_path};"
    )
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Correct CREATE TABLE statement for Access with proper data types
    create_table_query = f"""
    CREATE TABLE {table_name} (
        Product_Num TEXT PRIMARY KEY,
        Average_Demand DOUBLE
    );
    """
    try:
        cursor.execute(create_table_query)
        conn.commit()
    except Exception as e:
        print(f"Error creating table: {e}")

    # Insert each row from the DataFrame into the table
    for index, row in dataframe.iterrows():
        insert_query = f"""
        INSERT INTO {table_name} (Product_Num, Average_Demand)
        VALUES (?, ?)
        """
        try:
            cursor.execute(insert_query, row['Product_Num'], row['Average_Demand'])
            conn.commit()
        except Exception as e:
            print(f"Error inserting row: {e}")

    conn.close()
    print(f"Data successfully saved to {file_path} in the table {table_name}.")


def main():
    file_path = r"W:\zaherarm_khanah53\WARP2011W.mdb"
    table_name = "Product_Demand"  # Replace with your table name

    # Load data from MDB file
    data = load_data_from_mdb(file_path, table_name)
    print("Data loaded successfully.")

    # Calculate average demand
    average_demand = calculate_average_demand(data)
    print("Average demand for month 2 calculated.")
    print(average_demand)

    # Save the calculated results to MDB
    save_to_mdb(average_demand, file_path, "Average_Demand_Table")


if __name__ == "__main__":
    main()