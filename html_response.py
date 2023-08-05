def response(filename, prediction):
    html = f"""
        <html>
            <head>
                <title>Image prediction</title>
                <link rel="stylesheet" href="/static/styles/styles2.css">
            </head>
	        <body background="/static/images/prapor.jpg">
            	<br/>
            	<input type="button" onclick="history.back();" value="Повернутись на головну сторінку"/>
			    <p align="center"><img class="pos2" src="/static/upload/{filename}"></p>
		        <h2 align="center">{prediction}</h2>
            </body>
        </html>
        """

    return html
    