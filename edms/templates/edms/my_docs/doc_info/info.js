import * as React from 'react';
import Approvals from './doc_info_modules/approvals/approvals';
import Recipient from './doc_info_modules/recipient';
import Text from './doc_info_modules/text';
import Day from './doc_info_modules/day';
import Gate from './doc_info_modules/gate';
import CarryOut from './doc_info_modules/carry_out';
import Files from './doc_info_modules/files';
import ContractInfo from 'edms/templates/edms/my_docs/doc_info/doc_info_modules/contract_info';
import Stage from 'edms/templates/edms/my_docs/doc_info/doc_info_modules/stage';
import {getTextByQueue, getDayByQueue, getDatetimeByQueue} from 'templates/components/my_extras';
import ClientRequirementsInfo from 'edms/templates/edms/my_docs/doc_info/doc_info_modules/client_requirements_info';
import DocumentLink from 'edms/templates/edms/my_docs/doc_info/doc_info_modules/document_link';
import FoyerRanges from 'edms/templates/edms/my_docs/doc_info/doc_info_modules/foyer_ranges';
import CostRates from 'edms/templates/edms/my_docs/doc_info/doc_info_modules/cost_rates';
import Approved from 'edms/templates/edms/my_docs/doc_info/doc_info_modules/approved';

class Info extends React.Component {
  isFoyerRangesEditable = () => {
    const {expected_mark, viewer_is_author, stage} = this.props.info;

    return !!(stage !== 'confirm' && (expected_mark === 24 || viewer_is_author));
  };

  render() {
    const {info} = this.props;

    if (info.path) {
      return (
        <div>
          {/*Початкова інфа про документ:*/}
          <div>
            <span className='font-weight-bold'>{info.type}</span>
          </div>
          <If condition={info.closed}>
            <div className='font-weight-bold text-danger'>Документ позначений автором як неактуальний</div>
          </If>
          <div>
            <span>
              №: {info.id}. Дата: {info.date}
            </span>
          </div>
          <div>
            Відповідальний:
            <span className='font-italic'> {info.responsible}</span>
          </div>

          {/* Модульна система */}
          <If condition={info.type_modules}>
            <For each='module' index='index' of={info.type_modules}>
              <div key={index}>
                <Choose>
                  <When condition={module.module === 'recipient'}>
                    <Recipient
                      recipient={{
                        name: info.recipient.name,
                        seat: info.recipient.seat
                      }}
                      fieldName={module.field_name}
                    />
                  </When>
                  <When condition={module.module === 'recipient_chief'}>
                    <Recipient
                      recipient={{
                        name: info.recipient_chief.name,
                        seat: info.recipient_chief.seat
                      }}
                      fieldName={module.field_name}
                    />
                  </When>
                  <When condition={['text', 'dimensions', 'packaging_type', 'select'].includes(module.module)}>
                    <Text text={getTextByQueue(info.text_list, index)} text_info={module} doc_info={info} />
                  </When>
                  <When condition={module.module === 'day'}>
                    <Day day={getDayByQueue(info.days, index)} fieldName={module.field_name} />
                  </When>
                  <When condition={module.module === 'datetime'}>
                    <Day day={getDatetimeByQueue(info.datetimes, index)} fieldName={module.field_name} />
                  </When>
                  <When condition={module.module === 'foyer_datetime'}>
                    <FoyerDatetimes datetimes={info.foyer_ranges} fieldName={module.field_name} />
                  </When>
                  <When condition={module.module === 'gate'}>
                    <Gate gate={info.gate} fieldName={module.field_name} />
                  </When>
                  <When condition={module.module === 'carry_out_items'}>
                    <CarryOut carryOutItems={info.carry_out_items} fieldName={module.field_name} />
                  </When>
                  <When condition={module.module === 'files' && info.old_files.length > 0}>
                    <Files files={info.old_files} fieldName={module.field_name} is_editable={module.is_editable} />
                  </When>
                  <When condition={module.module === 'approval_list'}>
                    <Approvals info={info} />
                  </When>
                  <When
                    condition={['mockup_type', 'mockup_product_type', 'counterparty', 'scope', 'law', 'doc_type_version'].includes(
                      module.module
                    )}
                  >
                    <Text text_info={module} text={info[module.module].name} doc_info={info} />
                  </When>
                  <When condition={module.module === 'product_type_sell'}>
                    <Text text_info={{field_name: 'Тип продукції', is_editable: false}} text={info.sub_product.product} doc_info={info} />
                    <Text
                      text_info={{field_name: 'Підтип продукції', is_editable: false}}
                      text={info.sub_product.sub_product}
                      doc_info={info}
                    />
                  </When>
                  <When condition={module.module === 'client'}>
                    <Text text_info={module} text={`${info.client.name} (${info.client.country})`} doc_info={info} />
                  </When>
                  <When condition={module.module === 'contract_link'}>
                    <ContractInfo contract={info.contract_link} fieldName={module.field_name} />
                  </When>
                  <When condition={module.module === 'choose_company'}>
                    <div>
                      Компанія:<span className='font-italic'> {info.company} "ПЛХК"</span>
                    </div>
                  </When>
                  <When condition={module.module === 'stage'}>
                    <Stage stage={info.stage} />
                  </When>
                  <When condition={module.module === 'client_requirements'}>
                    <ClientRequirementsInfo
                      fieldName={module.field_name}
                      crs={info.client_requirements}
                      ars={info.additional_requirements}
                      sub_product={info.sub_product.id}
                    />
                  </When>
                  <When condition={module.module === 'document_link'}>
                    <DocumentLink documentLink={info.document_link} fieldName='Тендер' />
                  </When>
                  <When condition={module.module === 'registration'}>
                    <Text text_info={module} text={info.registration_number} doc_info={info} />
                  </When>
                  <When condition={module.module === 'employee'}>
                    <Text text_info={module} text={info.employee.name} doc_info={info} />
                  </When>
                  <When condition={module.module === 'foyer_ranges'}>
                    <FoyerRanges
                      ranges={info.foyer_ranges}
                      doc_id={info.id}
                      queue={module.queue}
                      doc_type_version={info.doc_type_version.id}
                      editable={this.isFoyerRangesEditable()}
                    />
                  </When>
                  <When condition={module.module === 'cost_rates'}>
                    <CostRates module={module} costRates={info.cost_rates} />
                  </When>
                  <When condition={module.module === 'auto_approved' && info.meta_type_id !== 5}>
                    {/*Не показуємо в Договорах, хоча використовуємо на сервері*/}
                    <Approved signed={info.approved} />
                  </When>
                </Choose>
              </div>
            </For>
          </If>

          <If condition={info.approvals}>
            <Approvals info={info} />
          </If>

          {/*Резолюції керівника (показуються, якщо документ чекає позначку "Виконано")*/}
          {/*<If condition={info?.expected_mark === 11}>*/}
          {/*  <Resolutions path={info.path} />*/}
          {/*</If>*/}
        </div>
      );
    } else {
      return <div>Щось пішло не так, зверніться до адміністратора</div>;
    }
  }
}

export default Info;
