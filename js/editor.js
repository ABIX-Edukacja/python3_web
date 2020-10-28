var mainPath = "./sandbox/"

var basePath = 'https://cdn.rawgit.com/Petlja/pygame4skulpt/3435847b/pygame/';
var externalLibs = {
    './pygame.js': basePath + '__init__.js',
    './pygame/display.js': basePath + 'display.js',
    './pygame/draw.js': basePath + 'draw.js',
    './pygame/event.js': basePath + 'event.js',
    './pygame/font.js': basePath + 'font.js',
    './pygame/image.js': basePath + 'image.js',
    './pygame/key.js': basePath + 'key.js',
    './pygame/mouse.js': basePath + 'mouse.js',
    './pygame/time.js': basePath + 'time.js',
    './pygame/transform.js': basePath + 'transform.js',
    './pygame/version.js': basePath + 'version.js',
};


function resetTarget() {
    var selector = Sk.TurtleGraphics.target;
    var target = typeof selector === "string" ? document.getElementById(selector) : selector;
    // clear canvas container
    while (target.firstChild) {
        target.removeChild(target.firstChild);
    }
    return target;
}

function createArrows(div) {
    var arrows = new Array(4);
    var direction = ["left", "right", "up", "down"];
    $(div).addClass("d-flex justify-content-center");
    for (var i = 0; i < 4; i++) {
        arrows[i] = document.createElement("span");
        div.appendChild(arrows[i]);
        $(arrows[i]).addClass("btn btn-primary btn-arrow");
        var ic = document.createElement("i");
        $(ic).addClass("fas fa-arrow-" + direction[i]);
        arrows[i].appendChild(ic);
    }


    var swapIcon = function (id) {
        $(arrows[id].firstChild).removeClass("fa-arrow-" + direction[id]).addClass("fa-arrow-circle-" + direction[id]);
    }

    var returnIcon = function (id) {
        $(arrows[id].firstChild).removeClass("fa-arrow-circle-" + direction[id]).addClass("fa-arrow-" + direction[id]);
    }

    $(arrows[0]).on('mousedown', function () {
        Sk.insertEvent("left");
        swapIcon(0);
    });
    $(arrows[0]).on('mouseup', function () {
        returnIcon(0);
    });
    $(arrows[1]).on('mousedown', function () {
        Sk.insertEvent("right");
        swapIcon(1);
    });
    $(arrows[1]).on('mouseup', function () {
        returnIcon(1);
    });
    $(arrows[2]).on('mousedown', function () {
        Sk.insertEvent("up");
        swapIcon(2);
    });
    $(arrows[2]).on('mouseup', function () {
        returnIcon(2);
    });
    $(arrows[3]).on('mousedown', function () {
        Sk.insertEvent("down");
        swapIcon(3);
    });
    $(arrows[3]).on('mouseup', function () {
        returnIcon(3);
    });

    $(document).keydown(function (e) {
        switch (e.which) {
            case 37:
                swapIcon(0);
                break;
            case 38:
                swapIcon(2);
                break;
            case 39:
                swapIcon(1);
                break;
            case 40:
                swapIcon(3);
                break;
        }
    });

    $(document).keyup(function (e) {
        switch (e.which) {
            case 37:
                returnIcon(0);
                break;
            case 38:
                returnIcon(2);
                break;
            case 39:
                returnIcon(1);
                break;
            case 40:
                returnIcon(3);
                break;
        }
    });
};

function printString(text) {
    var output = document.getElementById("output");
    text = text.replace(/</g, '&lt;');
    output.innerHTML = output.innerHTML + text;
}

function clearOutput() {
    var output = document.getElementById("output");
    output.innerHTML = '';
}

function builtinRead(x) {
    console.log('Attempting to load: '+x)

    if (externalLibs[x] !== undefined) {
        return Sk.misceval.promiseToSuspension(
            fetch(externalLibs[x]).then(
                function (resp){ return resp.text(); }
        ));
    }

    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
        throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}

function addModal() {
    $(Sk.main_canvas).css("border", "1px solid blue");
    var currentTarget = resetTarget();

    var div1 = document.createElement("div");
    currentTarget.appendChild(div1);
    $(div1).addClass("modal");
    $(div1).css("text-align", "center");

    var btn1 = document.createElement("span");
    $(btn1).addClass("btn btn-primary btn-sm pull-right");
    $(btn1).attr("data-dismiss", "modal");
    var ic = document.createElement("i");
    $(ic).addClass("fas fa-times");
    btn1.appendChild(ic);

    $(btn1).on('click', function (e) {
        try {
            Sk.insertEvent("quit");
        } catch(err) {
            console.log(err)
        }
    });

    var div2 = document.createElement("div");
    $(div2).addClass("modal-dialog modal-lg");
    $(div2).css("display", "inline-block");
    $(div2).width(self.width + 42);
    $(div2).attr("role", "document");
    div1.appendChild(div2);

    var div3 = document.createElement("div");
    $(div3).addClass("modal-content");
    div2.appendChild(div3);

    var div4 = document.createElement("div");
    $(div4).addClass("modal-header d-flex justify-content-between");
    var div5 = document.createElement("div");
    $(div5).addClass("modal-body");
    var div6 = document.createElement("div");
    $(div6).addClass("modal-footer");
    var div7 = document.createElement("div");
    $(div7).addClass("col-md-8");
    var div8 = document.createElement("div");
    $(div8).addClass("col-md-4");
    var header = document.createElement("h5");
    Sk.title_container = header;
    $(header).addClass("modal-title");


    div3.appendChild(div4);
    div3.appendChild(div5);
    div3.appendChild(div6);

    div4.appendChild(header);
    div4.appendChild(btn1);
    // div7.appendChild(header);
    // div8.appendChild(btn1);

    div5.appendChild(Sk.main_canvas);

    createArrows(div6);
    $(div1).modal({
        backdrop: 'static',
        keyboard: false
    });
}

function runCode() {
    Sk.main_canvas = document.createElement("canvas");
    
    Sk.quitHandler = function () {
        $('.modal').modal('hide');
    };
        
    var prog = ace.edit("editor").getValue();

    if (prog.includes("import pygame")) {
        addModal();
    }

    Sk.misceval.asyncToPromise(function () {
        try {
            return Sk.importMainWithBody("<stdin>", false, prog, true);
        } catch (e) {
            alert(e)
        }
    });
}

$(document).ready(function() {

    var editor = ace.edit("editor");
    editor.setTheme("ace/theme/chrome");
    editor.session.setMode("ace/mode/python");

    document.getElementById("editor").style['width'] = document.getElementById("editorsplace").offsetWidth;
    document.getElementById("editor").style['height'] = 0.7 * window.innerHeight;
    document.getElementById("editor").style['margin'] = "0 auto";
    document.getElementById("output").style['height'] = 0.7 * window.innerHeight;

    (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';
    Sk.configure({
        read: builtinRead,
        output: printString,
        __future__: Sk.python3
    });
    $("#runbutton").click(function () {
        runCode();
    });

    
    var sourcePath = mainPath+"00_empty.py";
    if (window.location.search.substring(1).length > 0) {
        sourcePath = mainPath + window.location.search.substring(1)
    }

    $.get(sourcePath, {}, function (data) {
        editor.setValue(data, -1);
    });

    var md = new Remarkable();
    instructionSourcePath = sourcePath.replace(new RegExp('.py$'), '.md');
    $.ajax({
        url: instructionSourcePath,
        type: 'GET',
        success: function(data){ 
            data = md.render(data)
            $('#instruction').html(data);
        },
        error: function() {
            instructionSourcePath = instructionSourcePath.replace(new RegExp('.md$'), '.txt');
            $.ajax({
                url: instructionSourcePath,
                type: 'GET',
                success: function (data) {
                    data = data.replace(/\r?\n/g, '<br />');
                    $('#instruction').html(data);
                },
                error: function() { $('#instruction').html("Brak przypisanej instrukcji do pliku.") }
            })
        }
    });
})