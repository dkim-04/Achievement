import pandas as pd 
import os

def divide_large_file_to_small_files(root_folder_path, output_folder_path):   
    # 출력 폴더가 존재하지 않으면 생성
    os.makedirs(output_folder_path, exist_ok=True)
    csv_files = []
    
    # 폴더 내부의 모든 CSV 파일 탐색
    for folder_path, subfolders, filenames in os.walk(root_folder_path):
        for filename in filenames:
            if filename.lower().endswith('.csv'):
                full_path = os.path.join(folder_path, filename)
                csv_files.append(full_path)
    
    # 각 CSV 파일에 대해 새로운 폴더 생성 및 파일 나누기
    for file_path in csv_files:
         # 원본 파일의 폴더 경로에서 root_folder_path 부분을 제거하여 상대 경로 생성
        relative_folder = os.path.relpath(os.path.dirname(file_path), root_folder_path)
        # output_folder_path에 상대 경로를 추가하여 새로운 폴더 경로 생성
        new_folder_path = os.path.join(output_folder_path, relative_folder, os.path.basename(file_path).replace('.csv', ''))
        # 새로운 폴더가 존재하지 않으면 생성
        
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
            print(f"폴더 생성 완료: {new_folder_path}")
        else:
            print(f"폴더가 이미 존재합니다: {new_folder_path}")
        
        # CSV 파일 읽기 및 나누기
        try:
            # Chunk 단위로 CSV 파일 읽기
            chunk_size = 1000000
            chunk_number = 1
            
            for chunk in pd.read_csv(file_path, chunksize=chunk_size,low_memory=False):
                # 특정 열을 제외 (열 이름 리스트가 제공된 경우)
                if columns_to_exclude:
                    # 열 이름을 소문자로 변환하여 columns_to_exclude와 비교
                    columns_to_exclude_lower = [col.lower() for col in columns_to_exclude]
                    chunk = chunk.drop(columns=[col for col in chunk.columns if col.lower() in columns_to_exclude_lower], errors='ignore')
                
                chunk_file_name = f"{name}_part_{chunk_number}.csv"
                chunk_file_path = os.path.join(new_folder_path, chunk_file_name)
                
                # 분할된 파일 저장
                chunk.to_csv(chunk_file_path, index=False)
                print(f"파일 저장 완료: {chunk_file_path}")
                
                chunk_number += 1
                
        except Exception as e:
            print(f"파일 처리 중 오류 발생: {e}")

# 경로 설정
root_folder_path = '/mnt/disk/disk02/sk_origin/'
output_folder_path = '/mnt/disk/disk02/divided_sk_car/'
# 제외할 열 리스트 설정 (예시: 'column_to_exclude' 열 제외)
columns_to_exclude = ['B_MAX_TEMP_MODUL_NO','B_MIN_TEMP_MODUL_NO','B_MAX_TEMP_PACK_NO','B_MIN_TEMP_PACK_NO','b_accum_recover_brake_quan','B_ASSIST_BATT_VOLT','B_INVERTER_CAPA_VOLT','B_MOTER_RPM'
,'B_HEATER1_TEMP','B_MAX_HEAT_CELL_NO','b_cell_balance_sts','b_cell_balance_cnt','b_slow_charg_cnt','b_fast_charg_cnt','b_accum_slow_charg_energy','b_accum_fast_charg_energy',
'B_COOLANT_INLET_TEMP','V_ACCEL_PEDAL_DEPTH','B_BATTERY_MOD','b_main_relay_on_error_sts','b_bms_alert_error_sts','b_bms_fusion_error_sts','b_opd_on_sts','b_opd_on_error_sts','b_wintermod_unInstall_sts'
,'b_mcu_control_error_sts','b_fast_charg_process_error_sts','b_fast_relay_on_sts','b_slow_charg_con_error_sts','m_mcu_fault_sts','m_mcu_torque_limit_sts','m_moter_controlable_sts01','m_mcu_engine_alert_lamp_sts',
'm_mcu_service_alert_lamp_sts','m_mcu_normal_sts','m_moter_controlable_sts02','m_mcu_main_relay_off_req_right','m_moter_pwm_sts','o_obc_inner_dc_volt','o_obc_dc_volt','o_obc_fault_sts','o_service_lamp_req'
,'o_assist_batt_soc','o_assist_batt_temp','v_bake_a_sts','v_bake_b_sts','v_accel_pedal_depth','v_ev_ready_sts','a_pm_sensor','c_mileage','cc_power_send_mod_init','cc_power_send_mod_Charg',
'cc_power_send_mod_V2L'	,'cc_power_send_mod_V2V','cc_evse_inout','cc_slow_charg_tt_cnt','cc_fast_charg_tt_cnt','cc_slow_charg_tt_hour','cc_fast_charg_tt_hour','cc_after_slow_charg_min','cc_after_fast_charg_min'
,'ps_column_torque','ps_steer_angle','ps_column_speed','bc_fl_wheel_speed','bc_fr_wheel_speed','bc_rl_wheel_speed','bc_rr_wheel_speed','tp_base_front_pressure','tp_base_rear_pressure','tp_fl_pressure'	
,'tp_fl_temp','tp_fr_pressure','tp_fr_temp','tp_rl_pressure','tp_rl_temp','tp_rr_pressure','tp_rr_temp','ii_door_act_switch','b_cell_temp_pack_no1','b_cell_temp_pack_no2','b_cell_temp_pack_no3','b_cell_temp_pack_no4','b_cell_temp_modul_no1'
,'b_cell_temp_modul_no2','b_cell_temp_modul_no3','b_cell_temp_modul_no4'
]

# 함수 호출
divide_large_file_to_small_files(root_folder_path, output_folder_path)
