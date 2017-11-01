function isValidDate() {
    var date = $("#date").val();
    var valid = true;

    date = date.split("-");

    var year = parseInt(date[0]);
    var month   = parseInt(date[1]);
    var day  = parseInt(date[2]);

    if(isNaN(month) || isNaN(day) || isNaN(year)) valid = false;

    if((month < 1) || (month > 12)) valid = false;
    else if((day < 1) || (day > 31)) valid = false;
    else if(((month == 4) || (month == 6) || (month == 9) || (month == 11)) && (day > 30)) valid = false;
    else if((month == 2) && (((year % 400) == 0) || ((year % 4) == 0)) && ((year % 100) != 0) && (day > 29)) valid = false;
    else if((month == 2) && ((year % 100) == 0) && (day > 29)) valid = false;
    else if((month == 2) && (day > 28)) valid = false;
    else if(year < 2000) valid = false;
    if (false==valid)
        alert("буруу байна. жишээ 12/24/2017");
}   

function isValidtime() {
    var time = $("#time").val();
    var time_valid = true;

    time = time.split(":");

    var tsag = parseInt(time[0]);
    var min   = parseInt(time[1]);
    if(isNaN(tsag) || isNaN(min) ) time_valid = false;

    if((tsag < 0 ) || (tsag > 24)) time_valid = false;
    else if((min < 0) || (min > 60)) time_valid = false;
    if (false==time_valid)
        alert("цаг буруу байна. жишээ 15:58");
}