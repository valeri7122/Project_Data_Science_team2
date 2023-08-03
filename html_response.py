def response(filename, prediction):
    html = f"""
        <html>
            <head>
                <title>Image prediction</title>
            </head>
	        <body bgcolor=blue>
            	<br/>
            	<input type="button" onclick="history.back();" value="Повернутись на головну сторінку"/>
                <br/><br/><br/>
			    <p align="center"><img class="pos2" src="/static/upload/{filename}" width="350" 
		        height="250" align="middle"></p><br/>
		        <h1 align="center"><font size="10" color=yellow face="Arial">{prediction}</font></h1>
            </body>
        </html>
        """

    return html
    
