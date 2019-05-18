<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css" integrity="sha384-oS3vJWv+0UjzBfQzYUhtDYW+Pj2yciDJxpsK1OYPAYjqT085Qq/1cq5FLXAZQ7Ay" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css?family=Kristi|Gugi" rel="stylesheet">
    <link rel="stylesheet" href="../static/css/test.css">
</head>

<body id="bg-color">
    <div id="main-menu-text">
        <a class="main-menu-item" href="/region" style="margin-right:5rem;">Home</a>
        <form action="/search">
            <button id="header-search-icon" class="search-btn btn-default" type="submit"><i class="fa fa-search"></i>
            </button>
            <input name="search" style="display" class="search-bar" type="text" placeholder="Search something here">
        </form>
        <a class="main-menu-item" href="/login">Login</a>
        <a class="main-menu-item" href="/register">Register</a>
    </div>
    <div class="bg-image">
        <div style="width: 100%;max-height: 100%;padding-top: 6%">
            <a href="#div-button-down">
                <div class="container btn" style="width: 80%;left: 10%;max-height: 100px;margin: 0">
                        <img src="../static/image/breakfast_kit8-net.png" style="max-height: 200px">
                        <button class="btn active" onclick="filterSelection('all')" style="color:white ;text-shadow:2px 2px black;">Show all</button>
                </div>
            </a>
            <a href="#div-button-down">                
                <div class="container btn" style="position:absolute;width: 25%;height: 70%;left: 10%;">
                        <img src="../static/image/toaster_and_toast_kit8-net.png" style="height: 100%">
                        <button class="btn" onclick="filterSelection('breakfast')" style="color:white ;text-shadow:2px 2px black;">Breakfast</button>
                    </div>
            </a>
            <a href="#div-button-down">                
                <div class="container btn" style="width:25%; left:37.5%">
                        <img src="../static/image/kitchen_pattern_2_kit8-net.png">
                        <button class="btn" onclick="filterSelection('lunch')" style="color:white ;text-shadow:2px 2px black;">Lunch</button>
                    </div>
            </a>
            <a href="#div-button-down">                
                <div class="container btn" style="width:25%; left:37.5%;height: 180px">
                        <img src="../static/image/equipment_fastfood_kit8-net.png">
                        <button class="btn" onclick="filterSelection('dessert_drink')" style="color:white ;text-shadow:2px 2px black;">Dessert/Drink</button>
                    </div>
            </a>
            <a href="#div-button-down">                
                <div class="container btn" style="position :absolute; width:25%; left:65%; top:26.4%; height: 71%;">
                        <img src="../static/image/food_kit8-net.png" style="height: 100%; padding-top : 3.4%;">
                        <button class="btn" onclick="filterSelection('dinner')" style="color:white ;text-shadow:2px 2px black;">Dinner</button>
                    </div>
            </a>
        </div>
    </div>

    <div id="div-button-down">
        <i id="button-down" class="fas fa-angle-down fa-2x"></i>
        <h1 style="margin: 0; margin-bottom : 17px;">RECIPES</h1>
    </div>

    {% for food in foods %} 
    
    {% if food.type == "breakfast" %}
    
    <div class="container">
        <div class="filterDiv breakfast">
            <div id="bg-item">
                <img id="img-odd-item" src="{{ food.link }}">
                <div id="describe-odd-item">
                    <h2>{{ food.title }}</h2>
                    <h2>Description:</h2>
                    <h6 style="margin:0;">{{ food.description }}</h6>
                </div>
                <a id="details-button" href="/food/{{ food._id }}">More Details</a>
            </div>
        </div>
    </div>
    {% elif food.type == "lunch" %}
    <div class="container">
        <div class="filterDiv lunch">
            <div id="bg-item">
                <img id="img-odd-item" src="{{ food.link }}">
                <div id="describe-odd-item">
                    <h2>{{ food.title }}</h2>
                    <h2>Description:</h2>
                    <h6 style="margin:0;">{{ food.description }}</h6>
                </div>
                <a id="details-button" href="/food/{{ food._id }}">More Details</a>
            </div>
        </div>
    </div>
    {% elif food.type == "dinner" %}
    <div class="container">
        <div class="filterDiv dinner">
            <div id="bg-item">
                <img id="img-odd-item" src="{{ food.link }}">
                <div id="describe-odd-item">
                    <h2>{{ food.title }}</h2>
                    <h2>Ingredients:</h2>
                    <h6 style="margin:0;">{{ food.description }}</h6>
                </div>
                <a id="details-button" href="/food/{{ food._id }}">More Details</a>
            </div>
        </div>
    </div>
    {% else %}
    <div class="container">
        <div class="filterDiv dessert">
            <div id="bg-item">
                <img id="img-odd-item" src="{{ food.link }}">
                <div id="describe-odd-item">
                    <h2>{{ food.title }}</h2>
                    <h2>Ingredients:</h2>
                    <h6 style="margin:0;">{{ food.description }}</h6>
                </div>
                <a id="details-button" href="/food/{{ food._id }}">More Details</a>
            </div>
        </div>
    </div>

    {% endif %} 
    {% endfor %}
    <script>
        filterSelection("all")

        function filterSelection(c) {
            var x, i;
            x = document.getElementsByClassName("filterDiv");
            if (c == "all") c = "";
            for (i = 0; i < x.length; i++) {
                w3RemoveClass(x[i], "show");
                if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
            }
        }

        function w3AddClass(element, name) {
            var i, arr1, arr2;
            arr1 = element.className.split(" ");
            arr2 = name.split(" ");
            for (i = 0; i < arr2.length; i++) {
                if (arr1.indexOf(arr2[i]) == -1) {
                    element.className += " " + arr2[i];
                }
            }
        }

        function w3RemoveClass(element, name) {
                var i, arr1, arr2;
                arr1 = element.className.split(" ");
                arr2 = name.split(" ");
                for (i = 0; i < arr2.length; i++) {
                    while (arr1.indexOf(arr2[i]) > -1) {
                        arr1.splice(arr1.indexOf(arr2[i]), 1);
                    }
                }
                element.className = arr1.join(" ");
            }
            // Add active class to the current button (highlight it)
        var btnContainer = document.getElementById("myBtnContainer");
        var btns = btnContainer.getElementsByClassName("btn");
        for (var i = 0; i < btns.length; i++) {
            btns[i].addEventListener("click", function() {
                var current = document.getElementsByClassName("active");
                current[0].className = current[0].className.replace(" active", "");
                this.className += " active";
            });
        }
    </script>

</body>

</html>
