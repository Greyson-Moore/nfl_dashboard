//prepares the webpage script
$(document).ready(function () {
    position = 'qb_'
    year = '2020'
    //searches the filter-boxes and adjusts the query
    $("#search").click(function() {
        //checks the player position        
        $("#position").on("change",function(){
            position = $("#position").val();
        });
        //checks the statistic year
        $("#year").on("change",function(){
            year = $("#year").val();
        });
        
        //table variable
        var querytable = position + year
        //prints data if successful
        $.ajax({
            type: "GET",
            url: "/",
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({ "data": querytable }),
            
            success: function(returnedData) {
        
                console.log(returnedData);
                
            $("#output").text(`${returnedData}`);
            
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert("Status: " + textStatus);
                alert("Error: " + errorThrown);
            }
        });
    

        
    });

});
