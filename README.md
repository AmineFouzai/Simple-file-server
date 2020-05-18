# Simple-file-server
Simple file server to serve files  over HTTP protocol via two endpoints <a href="https://github.com/MedAmineFouzai/Simple-file-server">/download</a> and <a href="https://github.com/MedAmineFouzai/Simple-file-server">/upload </a>
<hr>
<h1>#setup:</h1>
<table>
<tr>
<td> 1)  git clone https://github.com/MedAmineFouzai/Simple-file-server</td>
</tr>
<tr>
<td> 2) cd Simple-file-server</td>
</tr>
<tr>
<td> 3) pip install pipenv</td>
</tr>
</tr>
<td> 4) pipenv --python 3.6</td>
</tr>
<tr>
<td> 5) pipenv install - r requirements.txt</td>
</tr>
<tr>
  <td>
    6) run project with <a href="https://pypi.org/project/torn/">torn cli</a> : <b>#command: [ torn run ] </b>  </td>
 </tr>
</table>
<hr>
<h3>#Requesting Endpoints:</h3>
<h4>-To download data from a server, the client initiates a connection to the server and typically sends a HTTP GET request which just asks the server to provide specific data.
<h4/>
<h4>-To upload data to a server, the client again initiates a connection to the server and then typically sends a HTTP POST request which contains the data to be uploaded. The server knows how to handle such a request and stores the data.
</h4>
