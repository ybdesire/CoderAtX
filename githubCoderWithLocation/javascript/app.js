$(document).ready(function () {

    $.getJSON(
		"https://api.github.com/search/users?q=+location:%22Nan%20Jing%22&page=1&per_page=1000",
		function (data) {
		    var i = 0;
		    var str = "";
		    for (; i < data.items.length; i++) {
		        str = str + "<tr><td>" + data.items[i].html_url + "</td><td>31</td><td>32</td><td>33</td></tr>";
		    }
		    //add new row at the end of table
		    $("#infoTable tr:last").after(str);
		    //modify table row color
		    $("#infoTable tr:odd").addClass("todd");
		    $("#infoTable tr:even").addClass("teven");
		    //$("p").html(str);
		}
	);

    //parse email from url
    function getEmailFromURL(url)
    {
        $.get(url, function (data) {

        });
    }

});


