#target Illustrator

var requiredABsize = 24; //px
var activeDoc = app.activeDocument;

var abActive   = activeDoc.artboards[ activeDoc.artboards.getActiveArtboardIndex() ];
var abProps    = getArtboardBounds(abActive);
var scale	   = findRequiredScale(abProps);

if (scale  < 1)
{
	// select all items
	var items = activeDoc.pageItems;
	for(var i = 0;i < items.length;i++)
	{
		items[i].selected = true;
	}

	var selection = activeDoc.selection;

	// Check if anything is selected:
	if (selection.length > 0) 
	{
		
		// Loop over selected items:
		for (i = 0; i < selection.length; i++) 
		{
			selection[i].resize (scale*100, scale*100, true, true, true, true, scale*100, Transformation.DOCUMENTORIGIN);
		}
	} 
	
	activeDoc.fitArtboardToSelectedArt(activeDoc.artboards.getActiveArtboardIndex());
	app.executeMenuCommand("fitall");
	
}


// Artboard bounds helper (used above):
function getArtboardBounds(artboard) {

  var bounds = artboard.artboardRect,

      left   = bounds[0],
      top    = bounds[1],
      right  = bounds[2],
      bottom = bounds[3],

      width  = right - left,
      height = top - bottom,

      props  = {
        left   : left,
        top    : top,
        width  : width,
        height : height
      };

  return props;
}

function findRequiredScale(props) {
	var scale = Math.min(requiredABsize / props.height, requiredABsize / props.width);
	if (scale <1)
	return scale;
	else
	return 1;
}

