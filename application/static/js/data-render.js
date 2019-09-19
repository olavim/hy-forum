const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;

function renderEach(selector, cb) {
	$(selector).each(function () {
		$(this).text(cb(this));
	});
}

function utcToLocalCalendar(timestamp) {
	return moment.utc(timestamp).tz(tz).calendar();
}

$(document).ready(function () {
	renderEach('[data-timestamp]', elem => utcToLocalCalendar($(elem).data('timestamp')));
});
