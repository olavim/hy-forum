const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;

function renderEach(selector, cb) {
	$(selector).each(function () {
		$(this).text(cb(this));
	});
}

function utcToLocalCalendar(timestamp) {
	const m = timestamp === 'now' ? moment() : moment.utc(timestamp);
	return m.tz(tz).format('MMM Do YYYY, HH:mm');
}

$(document).ready(function () {
	renderEach('[data-timestamp]', elem => utcToLocalCalendar($(elem).data('timestamp')));
});
