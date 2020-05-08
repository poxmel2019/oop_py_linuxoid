"""Packages and modules"""
def data_collect():
    """Data collection for further processing"""
    print("Hello. You are going to wallpapering. We need some data")
    width = int(input('Width: '))
    length = int(input('Length: '))
    height = int(input('Height: '))
    paper_width = int(input('Paper width: '))
    paper_length = int(input('Paper length: '))
    

    return (width,length,height,paper_width,paper_length)
