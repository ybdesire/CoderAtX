$(document).ready(function () {

    $.getJSON(
		"https://api.github.com/search/users?q=+location:%22Nan%20Jing%22&page=1&per_page=1000",
		function (data) {
		    var i = 0;
		    var str = "";
		    for (; i < data.items.length; i++) {
		        str = str + data.items[i].html_url + "</br>"
		    }
		    $("p").html(str);
		}
	);
    //modify table row color
    $("#infoTable tr:odd").addClass("todd");
    $("#infoTable tr:even").addClass("teven");
    //add new row at the end of table
    var newRow = "<tr><td>30</td><td>31</td><td>32</td><td>33</td></tr>";
    $("#infoTable tr:last").after(newRow);
});


