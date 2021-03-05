import {store} from '@risingstack/react-easy-state';

const docInfoStore = store({
  doc: {},
  info: {},
  view: 'info', // info, new_document
  comment_to_answer: {
    id: 0,
    author: '',
    text: ''
  },
  signed_files: [],
  changed_files: {
    new_files: [],
    updated_files: [],
    updated_files_info: [],
    deleted_files: []
  },
  button_clicked: false,
  delegation_receiver_id: 0,

  clearChangedFiles: () => {
    docInfoStore.changed_files = {
      new_files: [],
      updated_files: [],
      updated_files_info: [],
      deleted_files: []
    };
  }
});

export default docInfoStore;
