const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;

function renderEach(selector, cb) {
	$(selector).each(function () {
		const text = cb(this);
		$(this).text(text);
	});
}

$(document).ready(function () {
	renderEach('[data-timestamp]', elem => {
		return moment.utc($(elem).data('timestamp')).tz(tz).calendar();
	});
});
