let gq1_submitted = false;
let gq2_submitted = false;
let gq3_submitted = false;

function sliderUpdate() {
    let cSlider = document.getElementById("c-slider");
    let cValue = document.getElementById("c-value");
    setSliderValues(cSlider, cValue);

    let javaSlider = document.getElementById("java-slider");
    let javaValue = document.getElementById("java-value");
    setSliderValues(javaSlider, javaValue);


    let jsSlider = document.getElementById("js-slider");
    let jsValue = document.getElementById("js-value");
    setSliderValues(jsSlider, jsValue);


    let tsSlider = document.getElementById("ts-slider");
    let tsValue = document.getElementById("ts-value");
    setSliderValues(tsSlider, tsValue);


    let cppSlider = document.getElementById("cpp-slider");
    let cppValue = document.getElementById("cpp-value");
    setSliderValues(cppSlider, cppValue);


    let linuxSlider = document.getElementById("linux-slider");
    let linuxValue = document.getElementById("linux-value");
    setSliderValues(linuxSlider, linuxValue);


    let sqlSlider = document.getElementById("sql-slider");
    let sqlValue = document.getElementById("sql-value");
    setSliderValues(sqlSlider, sqlValue);


    let htmlSlider = document.getElementById("html-slider");
    let htmlValue = document.getElementById("html-value");
    setSliderValues(htmlSlider, htmlValue);


    let csSlider = document.getElementById("cs-slider");
    let csValue = document.getElementById("cs-value");
    setSliderValues(csSlider, csValue);


    let pythonSlider = document.getElementById("python-slider");
    let pythonValue = document.getElementById("python-value");
    setSliderValues(pythonSlider, pythonValue);

}

const correctCodingSkillOrder = [
    '10',
    '2',
    '3',
    '8',
    '7',
    '6',
    '5',
    '4',
    '1',
    '9'
]

const correctSoftSkillOrder = [
    '5',
    '1',
    '2',
    '3',
    '4'
]

const correctHardSkillOrder = [
    '1',
    '4',
    '2',
    '3',
    '7',
    '6',
    '5'
]


function setSliderValues(slider, value) {
    if (value != null && slider != null) {
        value.innerHTML = slider.value;
        slider.oninput = function () {
            value.innerHTML = this.value;
        }
    }
}


function practice() {
    $("a").each(function () {
        let a = $(this);
        a.on('click', function () {
            const skill = a.attr('data-skill');
            const submission_url = a.attr('data-skill-practice-url')
            const username = a.attr('data-user-username')
            if (skill != undefined) {
                $.ajax({
                    url: submission_url,

                    data: {
                        skill: skill,
                        username: username,
                    },

                    type: "POST",

                    dataType: "json",

                    headers: {'X-CSRFToken': csrftoken},

                    context: this
                })
                // Code to run if the request succeeds (is done);
                // The response is passed to the function
                .done(function( json ) {
                 //alert("request received successfully");
                 if (json.success == 'success') {

                 }
                 else {
                     alert("Error" + json.error);
                 }
                })
                // Code to run if the request fails; the raw request and
                // status codes are passed to the function
                .fail(function( xhr, status, errorThrown ) {
                // alert( "Sorry, there was a problem!" );
                // console.log( "Error: " + errorThrown );
                // console.log( "Status: " + status );
                // console.dir( xhr );
                })
                // Code to run regardless of success or failure;
                .always(function( xhr, status ) {
                //alert( "The request is complete!" );
                });
            }
        })
    });
}


$(document).ready(function() {
    sliderUpdate();
    practice();
    $("#sortable").sortable();
    let check1 = $('#check-1');
    let check2 = $('#check-2');
    let check3 = $('#check-3');
    if (check1 != null) {
        check1.on('click', function () {
            const submission_url = $(this).attr('data-guessing-question-submission-url');
            let elements = $('#sortable').sortable('toArray', {attribute: 'data-id'});
            let j = 0;
            let number_wrong = 0;
            let question = 1;
            for (let i = 0; i < elements.length; i++) {
                if (elements[i] != correctCodingSkillOrder[j]) {
                    $("li[data-id='" + elements[i] + "']").css("background-color", "red");
                    number_wrong = number_wrong + 1;
                } else {
                    $("li[data-id='" + elements[i] + "']").css("background-color", "green");
                }
                j++;
            }
            $.ajax({
                url: submission_url,

                data: {
                    guess: elements.toString(),
                    number_wrong: number_wrong,
                    question: question,
                },

                type: "POST",

                dataType: "json",

                headers: {'X-CSRFToken': csrftoken},

                context: this
            })
              // Code to run if the request succeeds (is done);
              // The response is passed to the function
              .done(function( json ) {
                 //alert("request received successfully");
                 if (json.success == 'success') {
                     if (!gq1_submitted) {
                         let question_block = $("#question-block")
                         let url = question_block.attr("data-next-question-url")
                         let next_button = $("<a href=\"" + url + "\">Next Question</a>");
                         question_block.append(next_button);
                         gq1_submitted = true;
                     }
                 }
                 else {
                     alert("Error" + json.error);
                 }
              })
              // Code to run if the request fails; the raw request and
              // status codes are passed to the function
              .fail(function( xhr, status, errorThrown ) {
                alert( "Sorry, there was a problem!" );
                console.log( "Error: " + errorThrown );
                console.log( "Status: " + status );
                console.dir( xhr );
              })
              // Code to run regardless of success or failure;
              .always(function( xhr, status ) {
                //alert( "The request is complete!" );
              });
        });
    }
    if (check2 != null) {
        check2.on('click', function () {
            const submission_url = $(this).attr('data-guessing-question-submission-url');
            let elements = $('#sortable').sortable('toArray', {attribute: 'data-id'});
            let j = 0;
            let number_wrong = 0;
            let question = 2;
            for (let i = 0; i < elements.length; i++) {
                if (elements[i] != correctHardSkillOrder[j]) {
                    $("li[data-id='" + elements[i] + "']").css("background-color", "red");
                    number_wrong = number_wrong + 1;
                } else {
                    $("li[data-id='" + elements[i] + "']").css("background-color", "green");
                }
                j++;
            }
            $.ajax({
                url: submission_url,

                data: {
                    guess: elements.toString(),
                    number_wrong: number_wrong,
                    question: question,
                },

                type: "POST",

                dataType: "json",

                headers: {'X-CSRFToken': csrftoken},

                context: this
            })
              // Code to run if the request succeeds (is done);
              // The response is passed to the function
              .done(function( json ) {
                 //alert("request received successfully");
                 if (json.success == 'success') {
                     if (!gq2_submitted) {
                         let question_block = $("#question-block")
                         let url = question_block.attr("data-next-question-url")
                         let next_button = $("<a href=\"" + url + "\">Next Question</a>");
                         question_block.append(next_button);
                     }
                 }
                 else {
                     alert("Error" + json.error);
                 }
              })
              // Code to run if the request fails; the raw request and
              // status codes are passed to the function
              .fail(function( xhr, status, errorThrown ) {
                alert( "Sorry, there was a problem!" );
                console.log( "Error: " + errorThrown );
                console.log( "Status: " + status );
                console.dir( xhr );
              })
              // Code to run regardless of success or failure;
              .always(function( xhr, status ) {
                //alert( "The request is complete!" );
              });
        });
    }
    if (check3 != null) {
        check3.on('click', function () {
            const submission_url = $(this).attr('data-guessing-question-submission-url');
            let elements = $('#sortable').sortable('toArray', {attribute: 'data-id'});
            let j = 0;
            let number_wrong = 0;
            let question = 3;
            for (let i = 0; i < elements.length; i++) {
                if (elements[i] != correctSoftSkillOrder[j]) {
                    $("li[data-id='" + elements[i] + "']").css("background-color", "red");
                    number_wrong = number_wrong + 1;
                } else {
                    $("li[data-id='" + elements[i] + "']").css("background-color", "green");
                }
                j++;
            }
            $.ajax({
                url: submission_url,

                data: {
                    guess: elements.toString(),
                    number_wrong: number_wrong,
                    question: question,
                },

                type: "POST",

                dataType: "json",

                headers: {'X-CSRFToken': csrftoken},

                context: this
            })
              // Code to run if the request succeeds (is done);
              // The response is passed to the function
              .done(function( json ) {
                 //alert("request received successfully");
                 if (json.success == 'success') {
                     if (!gq3_submitted) {
                         gq3_submitted = true;
                         let question_block = $("#question-block")
                         let url = question_block.attr("data-resources-url")
                         let next_button = $("<a href=\"" + url + "\">Resources</a>");
                         question_block.append(next_button);
                     }
                 }
                 else {
                     alert("Error" + json.error);
                 }
              })
              // Code to run if the request fails; the raw request and
              // status codes are passed to the function
              .fail(function( xhr, status, errorThrown ) {
                alert( "Sorry, there was a problem!" );
                console.log( "Error: " + errorThrown );
                console.log( "Status: " + status );
                console.dir( xhr );
              })
              // Code to run regardless of success or failure;
              .always(function( xhr, status ) {
                //alert( "The request is complete!" );
              });
        });
    }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
