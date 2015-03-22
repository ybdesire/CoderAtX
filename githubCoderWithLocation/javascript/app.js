$(document).ready(function () {

    $.getJSON(
		"https://api.github.com/search/users?q=+location:%22Nan%20jing%22&page=1&per_page=100",
		function (data) {
		    var i = 0;
		    var str = "";
		    for (; i < data.items.length; i++) {
		        var id_email = "email_id_" + i.toString();
		        var githubURL = data.items[i].html_url;
                str = str + "<tr><td>" + githubURL + "</td><td id='" + id_email + "'>31</td><td>32</td><td>33</td></tr>";

		        //https://api.github.com/users/htoooth/events/public
                var vURL = githubURL.split('/');
                var user = vURL[vURL.length - 1];
                console.log(user);
                var urlForEmail = "https://api.github.com/users/" + user + '/events/public';
                getEmailFromURL(urlForEmail, i);
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
    function getEmailFromURL(url, i)
    {
        $.getJSON(url, function (data) {
            var j = 0;
            var email = "";

            for (; j < data.length; j++)
            {
                //if (typeof data[j].payload.commits.author.email != 'undefined')
                //console.log(data[j].payload.commits.author.email);
                if (data[j].hasOwnProperty("payload") && data[j].payload.hasOwnProperty("commits") && data[j].payload.commits[0].hasOwnProperty("author") && data[j].payload.commits[0].author.hasOwnProperty("email"))
                {
                    email = data[j].payload.commits[0].author.email;
                    if(email!="")
                    {
                        break;
                    }
                }
            }

            var id_email = "email_id_" + i.toString();
            $("#"+id_email).html(email)
        });
    }

});


