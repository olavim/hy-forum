const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;

function momentRender(elem) {
	const timestamp = $(elem).data('timestamp');
	$(elem).text(moment.tz(timestamp, tz).calendar());
	$(elem).removeClass('moment').show();
}

function momentRenderAll() {
	$('.moment').each(function() {
		momentRender(this);
	});
}

$(document).ready(function() {
	momentRenderAll();
});
