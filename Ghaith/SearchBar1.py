*{
margin: 0;
padding: 0;
}
           body{
background-image: url(1.jpg);  
-webkit-background-size:cover;
background-size:cover;
background-position: center center;
height: 100vh;
}

.wrapper{
width: 860px; 
margin: 0 auto;
}
.wrapper ul{
list-style: none;
margin-top: 2%;
}
.wrapper ul li {
background: #262626;
width: 170px;
border: 1px solid #fff;
height: 50px;
line-height: 50px;
text-align: center;
float: left;
color: #fff;
font-size: 16px;
position: relative;
font-family: poppins;
text-transform: uppercase;
font-weight: bold;
}
.wrapper ul li:hover{
background: crimson; 
}

.wrapper ul ul{
display: none;
}
.wrapper ul li:hover > ul{
display: block;
}
.wrapper ul ul ul{
margin-left: 170px;
top: 0;
position: absolute;
}
