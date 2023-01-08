function departmentInfo(name)
{
    if(name == "")
        return;

    var ajax = new XMLHttpRequest();

    ajax.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            $('#colldiv').html(ajax.reponseText);
        }
    };

    ajax.open("GET", "ajax_info.txt", true);
    ajax.send();
}
