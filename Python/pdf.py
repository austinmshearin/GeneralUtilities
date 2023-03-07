import pdfkit
import pandas as pd

# pdfkit parameters
path_wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
pdfkit_config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
pdfkit_options = {'quiet': ''}

def df_to_pdf(df: pd.DataFrame, filepath: str, header_1: str = None, header_2: str = None, \
              padding: dict = None, orientation: str = "Portrait"):
    """
    Outputs a pandas dataframe to a pdf report

    Parameters
    ----------
    df: pd.DataFrame
        Pandas dataframe of data
    filepath: str
        Full filepath of the output pdf file
    header_1: str = None
        Top most header of the pdf table
    header_2: str = None
        Second most header of the pdf table
    padding: dict = None
        Padding on columns for spacing by column name
    orientation: str = "Portrait"
        Orientation of pdf file. Can be Portrait or Landscape.
    """

    headers = [df.index.name] + df.columns.tolist()
    indexes = df.index.tolist()
    values = df.values.tolist()
    data = [[index]+value for index, value in zip(indexes,values)]
    
    output = "<html><head><meta name=\"pdfkit-orientation\" content=\"{}\"/></head><body>".format(orientation)
    if header_1 is not None:
        output += "<h1>{}</h1>".format(header_1)
    if header_2 is not None:
        output += "<h2>{}</h2>".format(header_2)
    output += "<table border=\"0\"><thead><tr style=\"text-align: left;\">"
    for header in headers:
        if padding is None:
            output += "<th>{}</th>".format(header)
        else:
            output += "<th style=\"padding-right:{0}px;\">{1}</th>".format(padding[header], header)
    output += "</tr></thead><tbody>"
    for row in data:
        output += "<tr>"
        for column_index, column in enumerate(row):
            if column_index == 0:
                output += "<th style=\"text-align: left;\">{}</th>".format(str(column))
            else:
                output += "<td>{}</td>".format(str(column))
        output += "</tr>"
    output += "</tbody></table></body></html>"
    pdfkit.from_string(output, filepath, configuration=pdfkit_config, options=pdfkit_options)

if __name__ == "__main__":
    import os
    data = {
        "index": [1,2,3,4,5,6,7,8,9,10], \
        "header_1": [1,2,3,4,5,6,7,8,9,10], \
        "header_2": [11,12,13,14,15,16,17,18,19,20], \
        "header_3": [21,22,23,24,25,26,27,28,29,30]
        }
    df = pd.DataFrame(data).set_index("index")
    filepath = os.path.join(os.getcwd(), "test.pdf")
    padding = {"index":10, "header_1": 25, "header_2": 50, "header_3": 25}
    #print(df.to_html())
    df_to_pdf(
        df = df,
        filepath = filepath,
        header_1 = "Header_1",
        header_2 = "TimeStamp",
        padding = padding,
        orientation = "Portrait"
    )
