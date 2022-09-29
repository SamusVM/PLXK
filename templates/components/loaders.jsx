import * as React from 'react';
import 'static/css/loader_style.css';

export function Loader() {
  return (
    <div className='css_loader'>
      <div className='loader' id='loader-1'>
        {' '}
      </div>
    </div>
  );
}

export function LoaderSmall() {
  return (
    <div className='mt-3 loader-small' id='loader-1'>
      {' '}
    </div>
  );
}

export function LoaderMini() {
  return (
    <div className='loader-mini'>
      ●
    </div>
  );
}
