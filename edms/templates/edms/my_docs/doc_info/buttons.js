'use strict';
import React from 'react';
import {view, store} from '@risingstack/react-easy-state';
import docInfoStore from './doc_info_modules/doc_info_store';

class Buttons extends React.Component {
  // отримує інформацію про документ в масиві info та створює відповідні кнопки для doc_info

  render() {
    const {info, isChief, deletable, onClick, archived} = this.props;
    const user_is_doc_author = info.author_seat_id === parseInt(localStorage.getItem('my_seat'));
  
    return (
      <>
        {/*Якщо є очікувана позначка:*/}
        <If condition={info.expected_mark}>
          {/* Дивимось, яку позначку очікує flow і показуємо відповідні кнопки */}
          <Choose>
            <When condition={info.expected_mark === 6}>
              {/* Не заперечую */}
              <button
                type='button'
                className='btn btn-secondary mr-1 mb-1'
                onClick={() => onClick(6)}
              >
                Не заперечую
              </button>
              <If condition={!user_is_doc_author}>
                <button
                  type='button'
                  className='btn btn-secondary mr-1 mb-1'
                  onClick={() => onClick(3)}
                >
                  Відмовити
                </button>
              </If>
            </When>
            <When condition={info.expected_mark === 2}>
              {/* Погоджую */}
              <button
                type='button'
                className='btn btn-secondary mr-1 mb-1'
                onClick={() => onClick(2)}
              >
                Погодити
              </button>
              <button
                type='button'
                className='btn btn-secondary mr-1 mb-1'
                onClick={() => onClick(3)}
              >
                Відмовити
              </button>
            </When>
            <When condition={info.expected_mark === 8}>
              {/* Ознайомлений */}
              <button
                type='button'
                className='btn btn-secondary mr-1 mb-1'
                onClick={() => onClick(8)}
              >
                Ознайомлений
              </button>
            </When>
            <When condition={info.expected_mark === 11}>
              {/* Виконано */}
              <button
                type='button'
                className='btn btn-secondary mr-1 mb-1'
                onClick={() => onClick(11)}
              >
                Виконано
              </button>
              <If condition={isChief === true}>
                {/* Якщо є підлеглі - додаємо резолюції */}
                <button
                  type='button'
                  className='btn btn-secondary mr-1 mb-1'
                  onClick={() => onClick(10)}
                >
                  Резолюція
                </button>
              </If>
            </When>
            <When condition={info.expected_mark === 17}>
              {/* Віза */}
              <button
                type='button'
                className='btn btn-secondary mr-1 mb-1'
                onClick={() => onClick(17)}
              >
                Візувати
              </button>
              <button
                type='button'
                className='btn btn-secondary mr-1 mb-1'
                onClick={() => onClick(3)}
              >
                Відмовити
              </button>
            </When>
            <When condition={info.expected_mark === 22}>
              {/* Прикріплення сканів підписаних документів */}
              <button
                type='button'
                className='btn btn-secondary mr-1 mb-1'
                onClick={() => onClick(22)}
              >
                Прикріпити скан-копії підписаних документів
              </button>
            </When>
          </Choose>
        </If>
        {/* Якщо автор я */}
        <If condition={user_is_doc_author}>
          {/*Якщо тип документа редагуємий*/}
          <If condition={docInfoStore?.info?.approved === false && docInfoStore?.info?.is_changeable && !info.archived}>
            <button
              type='button'
              className='btn btn-secondary mr-1 mb-1'
              onClick={() => (docInfoStore.view = 'new_document')}
            >
              Створити новий документ на основі цього
            </button>
          </If>
          {/* Якщо ніхто не встиг відреагувати - можна видалити документ */}
          <If condition={deletable === true}>
            <button
              type='button'
              className='btn btn-secondary mr-1 mb-1'
              onClick={() => onClick(13)}
            >
              Видалити
            </button>
          </If>
          {/* Додаємо кнопку Закрити */}
          <If condition={!archived && !info.archived}>
            {/*!archived - отримуємо з пропс, info.archived отримуємо з сервера, коли напряму шукаємо документ*/}
            <button
              type='button'
              className='btn btn-secondary mr-1 mb-1'
              onClick={() => onClick(7)}
            >
              В архів
            </button>
          </If>
        </If>
        {/* Якщо документ використовує approvals, додаємо кнопку "оновити файл" */}
        <If condition={info.type_id === 5 && !archived && !info.archived}>
          <button
            type='button'
            className='btn btn-secondary mr-1 mb-1'
            onClick={() => onClick(18)}
          >
            Додати/оновити документ
          </button>
        </If>
        {/* Кнопки "коментар", "на ознайомлення" та "файл" є завжди */}
        <button
          type='button'
          className='btn btn-secondary mr-1 mb-1'
          onClick={() => onClick(4)}
        >
          Коментар
        </button>
        <button
          type='button'
          className='btn btn-secondary mr-1 mb-1'
          onClick={() => onClick(15)}
        >
          На ознайомлення
        </button>
        <button
          type='button'
          className='btn btn-secondary mr-1 mb-1'
          onClick={() => onClick(12)}
        >
          Додати файл
        </button>
      </>
    );
  }

  static defaultProps = {
    isChief: false,
    deletable: false,
    onClick: () => {},
    info: [],
    archived: false,
  };
}

export default view(Buttons);
