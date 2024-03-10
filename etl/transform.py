from extract import extract_data

def transform_data(data):
    # remove the unecessary columns
    data = data.drop(['backdrop_path', 'poster_path', 'original_title'], axis=1)

    # remove missing values:
    data_new = data.dropna()   
    
    return data_new