/**
 * Based on the script resizeArtboards_CS4andUp.jsx by Carlos Canto 11/4/12
 */

#target Illustrator  

var OPTIONS = {
    size   : 512,
    width  : 512,
    height : 512
};

if (app.documents.length == 0) {
    alert("there are no open documents");
}
else {
    var idoc  = app.activeDocument;
    var title = "Resize All Artboards";

    // OPTIONS.size = Window.prompt ("Enter New Artboard size in pixels as WxH ( Example: 250x300 )", 24, title);
    
    // if (OPTIONS.size.indexOf('x') != -1) {
    //     var bits = OPTIONS.size.split('x');
    //     OPTIONS.width  = parseInt(bits[0]);
    //     OPTIONS.height = parseInt(bits[1]);
    // }
    // else {
    //     OPTIONS.width  = OPTIONS.size;
    //     OPTIONS.height = OPTIONS.size;
    // }

    try {
        var width  = OPTIONS.width;
        var height = OPTIONS.height;

        for (i=0; i<idoc.artboards.length; i++) {
            var abBounds = idoc.artboards[i].artboardRect; // left, top, right, bottom

            var ableft   = abBounds[0];
            var abtop    = abBounds[1];
            var abwidth  = abBounds[2] - ableft;
            var abheight = abtop- abBounds[3];

            var abctrx   = abwidth / 2 + ableft;
            var abctry   = abtop - abheight / 2;

            var ableft   = abctrx - width  / 2;
            var abtop    = abctry + height / 2;
            var abright  = abctrx + width  / 2;
            var abbottom = abctry - height / 2;

            idoc.artboards[i].artboardRect = [ableft, abtop, abright, abbottom];
        }
    }
    catch(e) {
        alert(e.message);
        /** Exist gracfully for now */
    }
}
