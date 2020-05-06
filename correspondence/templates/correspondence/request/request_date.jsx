'use strict';
import React from 'react';
import {view, store} from '@risingstack/react-easy-state';
import corrStore from '../store';

class RequestDate extends React.Component {
  onChange = (event) => {
    corrStore.request.request_date = event.target.value;
  };

  render() {
    return (
      <div className='form-inline mt-1'>
        <label className='text-nowrap mr-auto mr-md-1' htmlFor='request_date'>
          Дата отримання:
        </label>
        <input
          className='form-control'
          id='request_date'
          type='date'
          value={corrStore.request.request_date}
          onChange={this.onChange}
        />
      </div>
    );
  }
}

export default view(RequestDate);
