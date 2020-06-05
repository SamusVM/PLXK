'use strict';
import React from 'react';
import ReactToPrint from 'react-to-print-advanced';
import {faPrint} from '@fortawesome/free-solid-svg-icons';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import Info from './info';
import Path from './path';
// import photo from 'static/img/blank_header.png'

class DocumentPrint extends React.Component {
  hideStyle = {
    display: 'none'
  };

  printWindowStyle = {
    padding: '10px'
  };

  render() {
    const {doc, info} = this.props;

    return (
      <>
        <ReactToPrint
          trigger={() => (
            <a href='#' className='text-dark'>
              <FontAwesomeIcon icon={faPrint} />
            </a>
          )}
          content={() => this.componentRef}
          pageStyle={this.printWindowStyle}
        />

        <div style={this.hideStyle}>
          <div ref={(el) => (this.componentRef = el)}>
            <img src="../../../../static/img/blank_header.png" alt="Italian Trulli" style={{width: '100%'}} />
            
            <div className='css_border bg-light p-2 mt-2 mr-1'>
              <Info doc={doc} info={info} />
            </div>
            <Path path={info.path} />
          </div>
        </div>
      </>
    );
  }

  static defaultProps = {
    doc: [],
    info: []
  };
}

export default DocumentPrint;
