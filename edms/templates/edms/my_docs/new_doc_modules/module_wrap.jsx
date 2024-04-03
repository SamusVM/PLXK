'use strict';
import * as React from 'react';

function ModuleWrap(props) {

  return (
    <div className={`col-md-${props.columns} mb-0`}>
      <div className='css_edms_client_requirement'>
        {props.children}
      </div>
    </div>
  );
}

ModuleWrap.defaultProps = {
  columns: 12,
  module: ''
};

export default ModuleWrap;
