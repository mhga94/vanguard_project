def drop_null_rows(df, control_col : str):
    to_drop = df[df[control_col].isnull() == True].index
    new_df = df.drop(labels = list(to_drop), axis = 0)
    return new_df


def new_col_5_bins (data, column_name : str, new_column: str):
    # Assign boundaries
    boundary_1 = data[column_name].quantile(0.2) 
    boundary_2 = data[column_name].quantile(0.4) 
    boundary_3 = data[column_name].quantile(0.6) 
    boundary_4 = data[column_name].quantile(0.8) 
    boundary_5 = data[column_name].max()
    
    # Define a function to map the values to their respective bins
    def map_to_bin(value):
        if value <= boundary_1:
            return 1
        elif value <= boundary_2:
            return 2
        elif value <= boundary_3:
            return 3
        elif value <= boundary_4:
            return 4
        else:
            return 5

    # Apply the function to the column and assign the result to the new column
    data[new_column] = data[column_name].apply(map_to_bin)

    return data

def interpolator (original_values : list, all_values, new_range_min, new_range_max):
    m = interp1d([min(all_values),max(all_values)],[new_range_min,new_range_max])
    new_values = list(m(original_values))
    return new_values