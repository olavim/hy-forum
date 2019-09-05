import * as React from 'react';
import * as ReactDOM from 'react-dom';
import axios from 'axios';

(async() => {
	const res = await axios.get(window.env.API_URL);

	ReactDOM.render(
		<div style={{fontSize: '1.2rem', padding: '4rem'}}>
			<div style={{margin: '1rem'}}>Hello World from frontend!</div>
			<div style={{margin: '1rem'}}>{res.data} from backend!</div>
		</div>,
		document.getElementById('root') as HTMLElement
	);
})();
