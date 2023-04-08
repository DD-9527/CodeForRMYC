pid_pid = PIDCtrl()
pid_cpst = PIDCtrl()
pid_speed = PIDCtrl()
pid_pitch = PIDCtrl()
pid_Follow_Line = PIDCtrl()
list_LineList = RmList()
list_MarkerList = RmList()
list_k = RmList()
list_m = RmList()
list_MarkerList_2 = RmList()
list_sorted = RmList()
list_willshoot = RmList()
list_calc_num = RmList()
list_temp_marker = RmList()
variable_V_average = 0
variable_shotTime = 0
variable_device_qn = 0
variable_markerPosX = 0
variable_theta = 0
variable_markerPosY = 0
variable_max = 0
variable_Maker = 0
variable_b = 0
variable_mode = 0
variable_c = 0
variable_pidout = 0
variable_pitchVal = 0
variable_n = 0
variable_markerSizeW = 0
variable_MarkerSizeH = 0
variable_i = 0
variable_x = 0
variable_X = 0
variable_Y = 0
variable_K = 0
variable_v = 0
variable_done = 0
variable_hitting_num = 0
variable_found = 0
variable_done2 = 0
variable_UpperAngle = 0
variable_LeftAngle = 0
variable_sort_temp = 0
variable_sorting_num = 0
variable_sorting_index = 0
variable_timer1 = 0
variable_aa = 0
variable_bb = 0
variable_cc = 0
variable_dd = 0
variable_tempp = 0
variable_makeout = 0
variable_symbol_plus = 0
variable_symbol_minus = 0
variable_symbol_multiple = 0
variable_symbol_divide = 0
def user_defined_symbol_to_count():
    global variable_V_average
    global variable_shotTime
    global variable_device_qn
    global variable_markerPosX
    global variable_theta
    global variable_markerPosY
    global variable_max
    global variable_Maker
    global variable_b
    global variable_mode
    global variable_c
    global variable_pidout
    global variable_pitchVal
    global variable_n
    global variable_markerSizeW
    global variable_MarkerSizeH
    global variable_i
    global variable_x
    global variable_X
    global variable_Y
    global variable_K
    global variable_v
    global variable_done
    global variable_hitting_num
    global variable_found
    global variable_done2
    global variable_UpperAngle
    global variable_LeftAngle
    global variable_sort_temp
    global variable_sorting_num
    global variable_sorting_index
    global variable_timer1
    global variable_aa
    global variable_bb
    global variable_cc
    global variable_dd
    global variable_tempp
    global variable_makeout
    global variable_symbol_plus
    global variable_symbol_minus
    global variable_symbol_multiple
    global variable_symbol_divide
    global list_LineList
    global list_MarkerList
    global list_k
    global list_m
    global list_MarkerList_2
    global list_sorted
    global list_willshoot
    global list_calc_num
    global list_temp_marker
    global pid_pid
    global pid_cpst
    global pid_speed
    global pid_pitch
    global pid_Follow_Line
    variable_aa = list_calc_num[1]
    variable_bb = list_calc_num[2]
    variable_cc = list_calc_num[3]
    variable_dd = list_calc_num[4]
    if (variable_symbol_plus in (list_MarkerList)):
        user_defined_count1()

        user_defined_hit()
    else:
        if (variable_symbol_minus in (list_MarkerList)):
            user_defined_count2()

            user_defined_hit()
        else:
            if (variable_symbol_multiple in (list_MarkerList)):
                user_defined_count3()

                user_defined_hit()
            else:
                if (variable_symbol_divide in (list_MarkerList)):
                    user_defined_count4()

                    user_defined_hit()
                else:
                    media_ctrl.play_sound(rm_define.media_sound_solmization_3B)
def user_defined_count1():
    global variable_V_average
    global variable_shotTime
    global variable_device_qn
    global variable_markerPosX
    global variable_theta
    global variable_markerPosY
    global variable_max
    global variable_Maker
    global variable_b
    global variable_mode
    global variable_c
    global variable_pidout
    global variable_pitchVal
    global variable_n
    global variable_markerSizeW
    global variable_MarkerSizeH
    global variable_i
    global variable_x
    global variable_X
    global variable_Y
    global variable_K
    global variable_v
    global variable_done
    global variable_hitting_num
    global variable_found
    global variable_done2
    global variable_UpperAngle
    global variable_LeftAngle
    global variable_sort_temp
    global variable_sorting_num
    global variable_sorting_index
    global variable_timer1
    global variable_aa
    global variable_bb
    global variable_cc
    global variable_dd
    global variable_tempp
    global variable_makeout
    global variable_symbol_plus
    global variable_symbol_minus
    global variable_symbol_multiple
    global variable_symbol_divide
    global list_LineList
    global list_MarkerList
    global list_k
    global list_m
    global list_MarkerList_2
    global list_sorted
    global list_willshoot
    global list_calc_num
    global list_temp_marker
    global pid_pid
    global pid_cpst
    global pid_speed
    global pid_pitch
    global pid_Follow_Line
    list_willshoot=RmList()
    if variable_aa + (variable_bb + (variable_cc + variable_dd)) == 24:
        list_willshoot.append(variable_aa)
        list_willshoot.append(variable_symbol_plus)
        list_willshoot.append(variable_bb)
        list_willshoot.append(variable_symbol_plus)
        list_willshoot.append(variable_cc)
        list_willshoot.append(variable_symbol_plus)
        list_willshoot.append(variable_dd)
    else:
        if variable_aa + (variable_bb + variable_cc) == 24:
            list_willshoot.append(variable_aa)
            list_willshoot.append(variable_symbol_plus)
            list_willshoot.append(variable_bb)
            list_willshoot.append(variable_symbol_plus)
            list_willshoot.append(variable_cc)
        else:
            if variable_aa + (variable_bb + variable_dd) == 24:
                list_willshoot.append(variable_aa)
                list_willshoot.append(variable_symbol_plus)
                list_willshoot.append(variable_bb)
                list_willshoot.append(variable_symbol_plus)
                list_willshoot.append(variable_dd)
            else:
                if variable_aa + (variable_cc + variable_dd) == 24:
                    list_willshoot.append(variable_aa)
                    list_willshoot.append(variable_symbol_plus)
                    list_willshoot.append(variable_cc)
                    list_willshoot.append(variable_symbol_plus)
                    list_willshoot.append(variable_dd)
                else:
                    variable_makeout = 1
                    user_defined_atod()

                    while not variable_makeout >= 3:
                        variable_tempp = variable_aa
                        variable_aa = variable_bb
                        variable_bb = variable_cc
                        variable_cc = variable_dd
                        variable_dd = variable_tempp
                        user_defined_atod()

                        variable_makeout = variable_makeout + 1
def user_defined_hit():
    global variable_V_average
    global variable_shotTime
    global variable_device_qn
    global variable_markerPosX
    global variable_theta
    global variable_markerPosY
    global variable_max
    global variable_Maker
    global variable_b
    global variable_mode
    global variable_c
    global variable_pidout
    global variable_pitchVal
    global variable_n
    global variable_markerSizeW
    global variable_MarkerSizeH
    global variable_i
    global variable_x
    global variable_X
    global variable_Y
    global variable_K
    global variable_v
    global variable_done
    global variable_hitting_num
    global variable_found
    global variable_done2
    global variable_UpperAngle
    global variable_LeftAngle
    global variable_sort_temp
    global variable_sorting_num
    global variable_sorting_index
    global variable_timer1
    global variable_aa
    global variable_bb
    global variable_cc
    global variable_dd
    global variable_tempp
    global variable_makeout
    global variable_symbol_plus
    global variable_symbol_minus
    global variable_symbol_multiple
    global variable_symbol_divide
    global list_LineList
    global list_MarkerList
    global list_k
    global list_m
    global list_MarkerList_2
    global list_sorted
    global list_willshoot
    global list_calc_num
    global list_temp_marker
    global pid_pid
    global pid_cpst
    global pid_speed
    global pid_pitch
    global pid_Follow_Line
    if len(list_willshoot) > 1:
        variable_sorting_index = 1
        while not variable_sorting_index > len(list_willshoot):
            variable_hitting_num = list_willshoot[variable_sorting_index]
            if variable_hitting_num <= 9:
                variable_hitting_num = variable_hitting_num + 10
            variable_X = list_MarkerList[(list_MarkerList.index(variable_hitting_num)) + 1]
            variable_Y = list_MarkerList[(list_MarkerList.index(variable_hitting_num)) + 2]
            if variable_hitting_num >= 10 and variable_hitting_num <= 19:
                list_MarkerList[(list_MarkerList.index(variable_hitting_num))] = 9999
            gimbal_ctrl.angle_ctrl((96 / 0.9) * (variable_X - 0.5), 54 * (0.6 - variable_Y) + variable_UpperAngle)
            time.sleep(0.022)
            gun_ctrl.fire_once()
            time.sleep(0.18)
            variable_sorting_index = variable_sorting_index + 1
def user_defined_atod():
    global variable_V_average
    global variable_shotTime
    global variable_device_qn
    global variable_markerPosX
    global variable_theta
    global variable_markerPosY
    global variable_max
    global variable_Maker
    global variable_b
    global variable_mode
    global variable_c
    global variable_pidout
    global variable_pitchVal
    global variable_n
    global variable_markerSizeW
    global variable_MarkerSizeH
    global variable_i
    global variable_x
    global variable_X
    global variable_Y
    global variable_K
    global variable_v
    global variable_done
    global variable_hitting_num
    global variable_found
    global variable_done2
    global variable_UpperAngle
    global variable_LeftAngle
    global variable_sort_temp
    global variable_sorting_num
    global variable_sorting_index
    global variable_timer1
    global variable_aa
    global variable_bb
    global variable_cc
    global variable_dd
    global variable_tempp
    global variable_makeout
    global variable_symbol_plus
    global variable_symbol_minus
    global variable_symbol_multiple
    global variable_symbol_divide
    global list_LineList
    global list_MarkerList
    global list_k
    global list_m
    global list_MarkerList_2
    global list_sorted
    global list_willshoot
    global list_calc_num
    global list_temp_marker
    global pid_pid
    global pid_cpst
    global pid_speed
    global pid_pitch
    global pid_Follow_Line
    list_willshoot=RmList()
    if variable_aa * 10 + (variable_bb + (variable_cc + variable_dd)) == 24:
        list_willshoot.append(variable_aa)
        list_willshoot.append(variable_bb)
        list_willshoot.append(variable_symbol_plus)
        list_willshoot.append(variable_cc)
        list_willshoot.append(variable_symbol_plus)
        list_willshoot.append(variable_dd)
        variable_makeout = 3
    else:
        if variable_aa * 10 + (variable_bb + variable_cc) == 24:
            list_willshoot.append(variable_aa)
            list_willshoot.append(variable_bb)
            list_willshoot.append(variable_symbol_plus)
            list_willshoot.append(variable_cc)
            variable_makeout = 3
        else:
            if variable_aa * 10 + (variable_bb + variable_dd) == 24:
                list_willshoot.append(variable_aa)
                list_willshoot.append(variable_bb)
                list_willshoot.append(variable_symbol_plus)
                list_willshoot.append(variable_dd)
                variable_makeout = 3
            else:
                if (variable_aa * 10 + variable_cc) + (variable_bb + variable_dd) == 24:
                    list_willshoot.append(variable_aa)
                    list_willshoot.append(variable_cc)
                    list_willshoot.append(variable_symbol_plus)
                    list_willshoot.append(variable_bb)
                    list_willshoot.append(variable_symbol_plus)
                    list_willshoot.append(variable_dd)
                    variable_makeout = 3
                else:
                    if (variable_aa * 10 + variable_cc) + variable_bb == 24:
                        list_willshoot.append(variable_aa)
                        list_willshoot.append(variable_cc)
                        list_willshoot.append(variable_symbol_plus)
                        list_willshoot.append(variable_bb)
                        variable_makeout = 3
                    else:
                        if (variable_aa * 10 + variable_cc) + variable_dd == 24:
                            list_willshoot.append(variable_aa)
                            list_willshoot.append(variable_cc)
                            list_willshoot.append(variable_symbol_plus)
                            list_willshoot.append(variable_dd)
                            variable_makeout = 3
                        else:
                            if variable_aa * 10 + (variable_dd + (variable_cc + variable_bb)) == 24:
                                list_willshoot.append(variable_aa)
                                list_willshoot.append(variable_dd)
                                list_willshoot.append(variable_symbol_plus)
                                list_willshoot.append(variable_cc)
                                list_willshoot.append(variable_symbol_plus)
                                list_willshoot.append(variable_bb)
                                variable_makeout = 3
                            else:
                                if variable_aa * 10 + (variable_dd + variable_bb) == 24:
                                    list_willshoot.append(variable_aa)
                                    list_willshoot.append(variable_dd)
                                    list_willshoot.append(variable_symbol_plus)
                                    list_willshoot.append(variable_bb)
                                    variable_makeout = 3
                                else:
                                    if variable_aa * 10 + (variable_dd + variable_cc) == 24:
                                        list_willshoot.append(variable_aa)
                                        list_willshoot.append(variable_dd)
                                        list_willshoot.append(variable_symbol_plus)
                                        list_willshoot.append(variable_cc)
                                        variable_makeout = 3
                                    else:
                                        if (variable_aa * 10 + variable_bb) + (variable_cc * 10 + variable_dd) == 24:
                                            list_willshoot.append(variable_aa)
                                            list_willshoot.append(variable_bb)
                                            list_willshoot.append(variable_symbol_plus)
                                            list_willshoot.append(variable_cc)
                                            list_willshoot.append(variable_dd)
                                            variable_makeout = 3
                                        else:
                                            if (variable_aa * 10 + variable_bb) + (variable_dd * 10 + variable_cc) == 24:
                                                list_willshoot.append(variable_aa)
                                                list_willshoot.append(variable_bb)
                                                list_willshoot.append(variable_symbol_plus)
                                                list_willshoot.append(variable_dd)
                                                list_willshoot.append(variable_cc)
                                                variable_makeout = 3
                                            else:
                                                if (variable_aa * 10 + variable_cc) + (variable_bb * 10 + variable_dd) == 24:
                                                    list_willshoot.append(variable_aa)
                                                    list_willshoot.append(variable_cc)
                                                    list_willshoot.append(variable_symbol_plus)
                                                    list_willshoot.append(variable_bb)
                                                    list_willshoot.append(variable_dd)
                                                    variable_makeout = 3
                                                else:
                                                    if (variable_aa * 10 + variable_cc) + (variable_dd * 10 + variable_bb) == 24:
                                                        list_willshoot.append(variable_aa)
                                                        list_willshoot.append(variable_cc)
                                                        list_willshoot.append(variable_symbol_plus)
                                                        list_willshoot.append(variable_dd)
                                                        list_willshoot.append(variable_bb)
                                                        variable_makeout = 3
                                                    else:
                                                        if (variable_aa * 10 + variable_dd) + (variable_bb * 10 + variable_cc) == 24:
                                                            list_willshoot.append(variable_aa)
                                                            list_willshoot.append(variable_dd)
                                                            list_willshoot.append(variable_symbol_plus)
                                                            list_willshoot.append(variable_bb)
                                                            list_willshoot.append(variable_cc)
                                                            variable_makeout = 3
                                                        else:
                                                            if (variable_aa * 10 + variable_dd) + (variable_cc * 10 + variable_bb) == 24:
                                                                list_willshoot.append(variable_aa)
                                                                list_willshoot.append(variable_dd)
                                                                list_willshoot.append(variable_symbol_plus)
                                                                list_willshoot.append(variable_cc)
                                                                list_willshoot.append(variable_bb)
                                                                variable_makeout = 3
                                                            else:
                                                                pass
def user_defined_count2():
    global variable_V_average
    global variable_shotTime
    global variable_device_qn
    global variable_markerPosX
    global variable_theta
    global variable_markerPosY
    global variable_max
    global variable_Maker
    global variable_b
    global variable_mode
    global variable_c
    global variable_pidout
    global variable_pitchVal
    global variable_n
    global variable_markerSizeW
    global variable_MarkerSizeH
    global variable_i
    global variable_x
    global variable_X
    global variable_Y
    global variable_K
    global variable_v
    global variable_done
    global variable_hitting_num
    global variable_found
    global variable_done2
    global variable_UpperAngle
    global variable_LeftAngle
    global variable_sort_temp
    global variable_sorting_num
    global variable_sorting_index
    global variable_timer1
    global variable_aa
    global variable_bb
    global variable_cc
    global variable_dd
    global variable_tempp
    global variable_makeout
    global variable_symbol_plus
    global variable_symbol_minus
    global variable_symbol_multiple
    global variable_symbol_divide
    global list_LineList
    global list_MarkerList
    global list_k
    global list_m
    global list_MarkerList_2
    global list_sorted
    global list_willshoot
    global list_calc_num
    global list_temp_marker
    global pid_pid
    global pid_cpst
    global pid_speed
    global pid_pitch
    global pid_Follow_Line
    list_willshoot=RmList()
    variable_makeout = 1
    user_defined_atodminus()

    while not variable_makeout >= 3:
        variable_tempp = variable_aa
        variable_aa = variable_bb
        variable_bb = variable_cc
        variable_cc = variable_dd
        variable_dd = variable_tempp
        user_defined_atodminus()

        variable_makeout = variable_makeout + 1
def user_defined_Sort_number_into_list():
    global variable_V_average
    global variable_shotTime
    global variable_device_qn
    global variable_markerPosX
    global variable_theta
    global variable_markerPosY
    global variable_max
    global variable_Maker
    global variable_b
    global variable_mode
    global variable_c
    global variable_pidout
    global variable_pitchVal
    global variable_n
    global variable_markerSizeW
    global variable_MarkerSizeH
    global variable_i
    global variable_x
    global variable_X
    global variable_Y
    global variable_K
    global variable_v
    global variable_done
    global variable_hitting_num
    global variable_found
    global variable_done2
    global variable_UpperAngle
    global variable_LeftAngle
    global variable_sort_temp
    global variable_sorting_num
    global variable_sorting_index
    global variable_timer1
    global variable_aa
    global variable_bb
    global variable_cc
    global variable_dd
    global variable_tempp
    global variable_makeout
    global variable_symbol_plus
    global variable_symbol_minus
    global variable_symbol_multiple
    global variable_symbol_divide
    global list_LineList
    global list_MarkerList
    global list_k
    global list_m
    global list_MarkerList_2
    global list_sorted
    global list_willshoot
    global list_calc_num
    global list_temp_marker
    global pid_pid
    global pid_cpst
    global pid_speed
    global pid_pitch
    global pid_Follow_Line
    list_sorted=RmList()
    list_calc_num=RmList()
    variable_sorting_num = 10
    list_temp_marker=RmList(list_MarkerList)
    while not len(list_calc_num) >= 4:
        if (variable_sorting_num in (list_temp_marker)):
            list_sorted.append(variable_sorting_num)
            list_calc_num.append(variable_sorting_num - 10)
            list_temp_marker.pop((list_temp_marker.index(variable_sorting_num)))
        else:
            variable_sorting_num = variable_sorting_num + 1
def user_defined_detect():
    global variable_V_average
    global variable_shotTime
    global variable_device_qn
    global variable_markerPosX
    global variable_theta
    global variable_markerPosY
    global variable_max
    global variable_Maker
    global variable_b
    global variable_mode
    global variable_c
    global variable_pidout
    global variable_pitchVal
    global variable_n
    global variable_markerSizeW
    global variable_MarkerSizeH
    global variable_i
    global variable_x
    global variable_X
    global variable_Y
    global variable_K
    global variable_v
    global variable_done
    global variable_hitting_num
    global variable_found
    global variable_done2
    global variable_UpperAngle
    global variable_LeftAngle
    global variable_sort_temp
    global variable_sorting_num
    global variable_sorting_index
    global variable_timer1
    global variable_aa
    global variable_bb
    global variable_cc
    global variable_dd
    global variable_tempp
    global variable_makeout
    global variable_symbol_plus
    global variable_symbol_minus
    global variable_symbol_multiple
    global variable_symbol_divide
    global list_LineList
    global list_MarkerList
    global list_k
    global list_m
    global list_MarkerList_2
    global list_sorted
    global list_willshoot
    global list_calc_num
    global list_temp_marker
    global pid_pid
    global pid_cpst
    global pid_speed
    global pid_pitch
    global pid_Follow_Line
    gimbal_ctrl.yaw_ctrl(0)
    gimbal_ctrl.pitch_ctrl(variable_UpperAngle)
    list_willshoot=RmList()
    time.sleep(1)
    variable_done = 0
    list_MarkerList=RmList()
    while not len(list_MarkerList) >= 26:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
    user_defined_Sort_number_into_list()

    user_defined_symbol_to_count()

    time.sleep(0.75)
def user_defined_count3():
    global variable_V_average
    global variable_shotTime
    global variable_device_qn
    global variable_markerPosX
    global variable_theta
    global variable_markerPosY
    global variable_max
    global variable_Maker
    global variable_b
    global variable_mode
    global variable_c
    global variable_pidout
    global variable_pitchVal
    global variable_n
    global variable_markerSizeW
    global variable_MarkerSizeH
    global variable_i
    global variable_x
    global variable_X
    global variable_Y
    global variable_K
    global variable_v
    global variable_done
    global variable_hitting_num
    global variable_found
    global variable_done2
    global variable_UpperAngle
    global variable_LeftAngle
    global variable_sort_temp
    global variable_sorting_num
    global variable_sorting_index
    global variable_timer1
    global variable_aa
    global variable_bb
    global variable_cc
    global variable_dd
    global variable_tempp
    global variable_makeout
    global variable_symbol_plus
    global variable_symbol_minus
    global variable_symbol_multiple
    global variable_symbol_divide
    global list_LineList
    global list_MarkerList
    global list_k
    global list_m
    global list_MarkerList_2
    global list_sorted
    global list_willshoot
    global list_calc_num
    global list_temp_marker
    global pid_pid
    global pid_cpst
    global pid_speed
    global pid_pitch
    global pid_Follow_Line
    list_willshoot=RmList()
    if variable_aa * (variable_bb * (variable_cc * variable_dd)) == 24:
        list_willshoot.append(variable_aa)
        list_willshoot.append(variable_symbol_multiple)
        list_willshoot.append(variable_bb)
        list_willshoot.append(variable_symbol_multiple)
        list_willshoot.append(variable_cc)
        list_willshoot.append(variable_symbol_multiple)
        list_willshoot.append(variable_dd)
    else:
        if variable_aa * (variable_bb * variable_cc) == 24:
            list_willshoot.append(variable_aa)
            list_willshoot.append(variable_symbol_multiple)
            list_willshoot.append(variable_bb)
            list_willshoot.append(variable_symbol_multiple)
            list_willshoot.append(variable_cc)
        else:
            if variable_aa * (variable_bb * variable_dd) == 24:
                list_willshoot.append(variable_aa)
                list_willshoot.append(variable_symbol_multiple)
                list_willshoot.append(variable_bb)
                list_willshoot.append(variable_symbol_multiple)
                list_willshoot.append(variable_dd)
            else:
                if variable_aa * (variable_cc * variable_dd) == 24:
                    list_willshoot.append(variable_aa)
                    list_willshoot.append(variable_symbol_multiple)
                    list_willshoot.append(variable_cc)
                    list_willshoot.append(variable_symbol_multiple)
                    list_willshoot.append(variable_dd)
                else:
                    variable_makeout = 1
                    user_defined_atodby()

                    while not variable_makeout >= 3:
                        variable_tempp = variable_aa
                        variable_aa = variable_bb
                        variable_bb = variable_cc
                        variable_cc = variable_dd
                        variable_dd = variable_tempp
                        user_defined_atodby()

                        variable_makeout = variable_makeout + 1
def user_defined_count4():
    global variable_V_average
    global variable_shotTime
    global variable_device_qn
    global variable_markerPosX
    global variable_theta
    global variable_markerPosY
    global variable_max
    global variable_Maker
    global variable_b
    global variable_mode
    global variable_c
    global variable_pidout
    global variable_pitchVal
    global variable_n
    global variable_markerSizeW
    global variable_MarkerSizeH
    global variable_i
    global variable_x
    global variable_X
    global variable_Y
    global variable_K
    global variable_v
    global variable_done
    global variable_hitting_num
    global variable_found
    global variable_done2
    global variable_UpperAngle
    global variable_LeftAngle
    global variable_sort_temp
    global variable_sorting_num
    global variable_sorting_index
    global variable_timer1
    global variable_aa
    global variable_bb
    global variable_cc
    global variable_dd
    global variable_tempp
    global variable_makeout
    global variable_symbol_plus
    global variable_symbol_minus
    global variable_symbol_multiple
    global variable_symbol_divide
    global list_LineList
    global list_MarkerList
    global list_k
    global list_m
    global list_MarkerList_2
    global list_sorted
    global list_willshoot
    global list_calc_num
    global list_temp_marker
    global pid_pid
    global pid_cpst
    global pid_speed
    global pid_pitch
    global pid_Follow_Line
    list_willshoot=RmList()
    variable_makeout = 1
    user_defined_atoddivide()

    while not variable_makeout >= 3:
        variable_tempp = variable_aa
        variable_aa = variable_bb
        variable_bb = variable_cc
        variable_cc = variable_dd
        variable_dd = variable_tempp
        user_defined_atoddivide()

        variable_makeout = variable_makeout + 1
def user_defined_atoddivide():
    global variable_V_average
    global variable_shotTime
    global variable_device_qn
    global variable_markerPosX
    global variable_theta
    global variable_markerPosY
    global variable_max
    global variable_Maker
    global variable_b
    global variable_mode
    global variable_c
    global variable_pidout
    global variable_pitchVal
    global variable_n
    global variable_markerSizeW
    global variable_MarkerSizeH
    global variable_i
    global variable_x
    global variable_X
    global variable_Y
    global variable_K
    global variable_v
    global variable_done
    global variable_hitting_num
    global variable_found
    global variable_done2
    global variable_UpperAngle
    global variable_LeftAngle
    global variable_sort_temp
    global variable_sorting_num
    global variable_sorting_index
    global variable_timer1
    global variable_aa
    global variable_bb
    global variable_cc
    global variable_dd
    global variable_tempp
    global variable_makeout
    global variable_symbol_plus
    global variable_symbol_minus
    global variable_symbol_multiple
    global variable_symbol_divide
    global list_LineList
    global list_MarkerList
    global list_k
    global list_m
    global list_MarkerList_2
    global list_sorted
    global list_willshoot
    global list_calc_num
    global list_temp_marker
    global pid_pid
    global pid_cpst
    global pid_speed
    global pid_pitch
    global pid_Follow_Line
    list_willshoot=RmList()
    if (variable_aa * 10 + variable_bb) / variable_cc == 24:
        list_willshoot.append(variable_aa)
        list_willshoot.append(variable_bb)
        list_willshoot.append(variable_symbol_divide)
        list_willshoot.append(variable_cc)
        variable_makeout = 3
    else:
        if (variable_aa * 10 + variable_bb) / variable_dd == 24:
            list_willshoot.append(variable_aa)
            list_willshoot.append(variable_bb)
            list_willshoot.append(variable_symbol_divide)
            list_willshoot.append(variable_dd)
            variable_makeout = 3
        else:
            if (variable_aa * 10 + variable_cc) / variable_bb == 24:
                list_willshoot.append(variable_aa)
                list_willshoot.append(variable_cc)
                list_willshoot.append(variable_symbol_divide)
                list_willshoot.append(variable_bb)
                variable_makeout = 3
            else:
                if (variable_aa * 10 + variable_cc) / variable_dd == 24:
                    list_willshoot.append(variable_aa)
                    list_willshoot.append(variable_cc)
                    list_willshoot.append(variable_symbol_divide)
                    list_willshoot.append(variable_dd)
                    variable_makeout = 3
                else:
                    if (variable_aa * 10 + variable_dd) / variable_bb == 24:
                        list_willshoot.append(variable_aa)
                        list_willshoot.append(variable_dd)
                        list_willshoot.append(variable_symbol_divide)
                        list_willshoot.append(variable_bb)
                        variable_makeout = 3
                    else:
                        if (variable_aa * 10 + variable_dd) / variable_cc == 24:
                            list_willshoot.append(variable_aa)
                            list_willshoot.append(variable_dd)
                            list_willshoot.append(variable_symbol_divide)
                            list_willshoot.append(variable_cc)
                            variable_makeout = 3
                        else:
                            if (variable_aa * 100 + (variable_bb * 10 + variable_cc)) / variable_dd == 24:
                                list_willshoot.append(variable_aa)
                                list_willshoot.append(variable_bb)
                                list_willshoot.append(variable_cc)
                                list_willshoot.append(variable_symbol_divide)
                                list_willshoot.append(variable_dd)
                                variable_makeout = 3
                            else:
                                if (variable_aa * 100 + (variable_bb * 10 + variable_dd)) / variable_cc == 24:
                                    list_willshoot.append(variable_aa)
                                    list_willshoot.append(variable_bb)
                                    list_willshoot.append(variable_cc)
                                    list_willshoot.append(variable_symbol_divide)
                                    list_willshoot.append(variable_dd)
                                    variable_makeout = 3
                                else:
                                    if ((variable_aa * 10 + variable_bb) / variable_cc) / variable_dd == 24:
                                        list_willshoot.append(variable_aa)
                                        list_willshoot.append(variable_bb)
                                        list_willshoot.append(variable_symbol_divide)
                                        list_willshoot.append(variable_cc)
                                        list_willshoot.append(variable_symbol_divide)
                                        list_willshoot.append(variable_dd)
                                        variable_makeout = 3
                                    else:
                                        if (variable_aa * 100 + (variable_cc * 10 + variable_bb)) / variable_dd == 24:
                                            list_willshoot.append(variable_aa)
                                            list_willshoot.append(variable_bb)
                                            list_willshoot.append(variable_cc)
                                            list_willshoot.append(variable_symbol_divide)
                                            list_willshoot.append(variable_dd)
                                            variable_makeout = 3
                                        else:
                                            if (variable_aa * 100 + (variable_cc * 10 + variable_dd)) / variable_bb == 24:
                                                list_willshoot.append(variable_aa)
                                                list_willshoot.append(variable_bb)
                                                list_willshoot.append(variable_cc)
                                                list_willshoot.append(variable_symbol_divide)
                                                list_willshoot.append(variable_dd)
                                                variable_makeout = 3
                                            else:
                                                if (variable_aa * 100 + (variable_dd * 10 + variable_bb)) / variable_cc == 24:
                                                    list_willshoot.append(variable_aa)
                                                    list_willshoot.append(variable_bb)
                                                    list_willshoot.append(variable_cc)
                                                    list_willshoot.append(variable_symbol_divide)
                                                    list_willshoot.append(variable_dd)
                                                    variable_makeout = 3
                                                else:
                                                    if (variable_aa * 100 + (variable_dd * 10 + variable_cc)) / variable_bb == 24:
                                                        list_willshoot.append(variable_aa)
                                                        list_willshoot.append(variable_bb)
                                                        list_willshoot.append(variable_cc)
                                                        list_willshoot.append(variable_symbol_divide)
                                                        list_willshoot.append(variable_dd)
                                                        variable_makeout = 3
                                                    else:
                                                        if ((variable_aa * 10 + variable_cc) / variable_bb) / variable_dd == 24:
                                                            list_willshoot.append(variable_aa)
                                                            list_willshoot.append(variable_cc)
                                                            list_willshoot.append(variable_symbol_divide)
                                                            list_willshoot.append(variable_bb)
                                                            list_willshoot.append(variable_symbol_divide)
                                                            list_willshoot.append(variable_dd)
                                                            variable_makeout = 3
                                                        else:
                                                            if ((variable_aa * 10 + variable_dd) / variable_bb) / variable_cc == 24:
                                                                list_willshoot.append(variable_aa)
                                                                list_willshoot.append(variable_dd)
                                                                list_willshoot.append(variable_symbol_divide)
                                                                list_willshoot.append(variable_bb)
                                                                list_willshoot.append(variable_symbol_divide)
                                                                list_willshoot.append(variable_cc)
                                                                variable_makeout = 3
                                                            else:
                                                                pass
def user_defined_atodminus():
    global variable_V_average
    global variable_shotTime
    global variable_device_qn
    global variable_markerPosX
    global variable_theta
    global variable_markerPosY
    global variable_max
    global variable_Maker
    global variable_b
    global variable_mode
    global variable_c
    global variable_pidout
    global variable_pitchVal
    global variable_n
    global variable_markerSizeW
    global variable_MarkerSizeH
    global variable_i
    global variable_x
    global variable_X
    global variable_Y
    global variable_K
    global variable_v
    global variable_done
    global variable_hitting_num
    global variable_found
    global variable_done2
    global variable_UpperAngle
    global variable_LeftAngle
    global variable_sort_temp
    global variable_sorting_num
    global variable_sorting_index
    global variable_timer1
    global variable_aa
    global variable_bb
    global variable_cc
    global variable_dd
    global variable_tempp
    global variable_makeout
    global variable_symbol_plus
    global variable_symbol_minus
    global variable_symbol_multiple
    global variable_symbol_divide
    global list_LineList
    global list_MarkerList
    global list_k
    global list_m
    global list_MarkerList_2
    global list_sorted
    global list_willshoot
    global list_calc_num
    global list_temp_marker
    global pid_pid
    global pid_cpst
    global pid_speed
    global pid_pitch
    global pid_Follow_Line
    list_willshoot=RmList()
    if ((variable_aa * 10 + variable_bb) - variable_cc) - variable_dd == 24:
        list_willshoot.append(variable_aa)
        list_willshoot.append(variable_bb)
        list_willshoot.append(variable_symbol_minus)
        list_willshoot.append(variable_cc)
        list_willshoot.append(variable_symbol_minus)
        list_willshoot.append(variable_dd)
        variable_makeout = 3
    else:
        if (variable_aa * 10 + variable_bb) - variable_cc == 24:
            list_willshoot.append(variable_aa)
            list_willshoot.append(variable_bb)
            list_willshoot.append(variable_symbol_minus)
            list_willshoot.append(variable_cc)
            variable_makeout = 3
        else:
            if (variable_aa * 10 + variable_bb) - variable_dd == 24:
                list_willshoot.append(variable_aa)
                list_willshoot.append(variable_bb)
                list_willshoot.append(variable_symbol_minus)
                list_willshoot.append(variable_dd)
                variable_makeout = 3
            else:
                if ((variable_aa * 10 + variable_cc) - variable_bb) - variable_dd == 24:
                    list_willshoot.append(variable_aa)
                    list_willshoot.append(variable_cc)
                    list_willshoot.append(variable_symbol_minus)
                    list_willshoot.append(variable_bb)
                    list_willshoot.append(variable_symbol_minus)
                    list_willshoot.append(variable_dd)
                    variable_makeout = 3
                else:
                    if (variable_aa * 10 + variable_cc) - variable_bb == 24:
                        list_willshoot.append(variable_aa)
                        list_willshoot.append(variable_cc)
                        list_willshoot.append(variable_symbol_minus)
                        list_willshoot.append(variable_bb)
                        variable_makeout = 3
                    else:
                        if (variable_aa * 10 + variable_cc) - variable_dd == 24:
                            list_willshoot.append(variable_aa)
                            list_willshoot.append(variable_cc)
                            list_willshoot.append(variable_symbol_minus)
                            list_willshoot.append(variable_dd)
                            variable_makeout = 3
                        else:
                            if ((variable_aa * 10 + variable_dd) - variable_cc) - variable_bb == 24:
                                list_willshoot.append(variable_aa)
                                list_willshoot.append(variable_dd)
                                list_willshoot.append(variable_symbol_minus)
                                list_willshoot.append(variable_cc)
                                list_willshoot.append(variable_symbol_minus)
                                list_willshoot.append(variable_bb)
                                variable_makeout = 3
                            else:
                                if (variable_aa * 10 + variable_dd) - variable_bb == 24:
                                    list_willshoot.append(variable_aa)
                                    list_willshoot.append(variable_dd)
                                    list_willshoot.append(variable_symbol_minus)
                                    list_willshoot.append(variable_bb)
                                    variable_makeout = 3
                                else:
                                    if (variable_aa * 10 + variable_dd) - variable_cc == 24:
                                        list_willshoot.append(variable_aa)
                                        list_willshoot.append(variable_dd)
                                        list_willshoot.append(variable_symbol_minus)
                                        list_willshoot.append(variable_cc)
                                        variable_makeout = 3
                                    else:
                                        if (variable_aa * 10 + variable_bb) - (variable_cc * 10 + variable_dd) == 24:
                                            list_willshoot.append(variable_aa)
                                            list_willshoot.append(variable_bb)
                                            list_willshoot.append(variable_symbol_minus)
                                            list_willshoot.append(variable_cc)
                                            list_willshoot.append(variable_dd)
                                            variable_makeout = 3
                                        else:
                                            if (variable_aa * 10 + variable_bb) - (variable_dd * 10 + variable_cc) == 24:
                                                list_willshoot.append(variable_aa)
                                                list_willshoot.append(variable_bb)
                                                list_willshoot.append(variable_symbol_minus)
                                                list_willshoot.append(variable_dd)
                                                list_willshoot.append(variable_cc)
                                                variable_makeout = 3
                                            else:
                                                if (variable_aa * 10 + variable_cc) - (variable_bb * 10 + variable_dd) == 24:
                                                    list_willshoot.append(variable_aa)
                                                    list_willshoot.append(variable_cc)
                                                    list_willshoot.append(variable_symbol_minus)
                                                    list_willshoot.append(variable_bb)
                                                    list_willshoot.append(variable_dd)
                                                    variable_makeout = 3
                                                else:
                                                    if (variable_aa * 10 + variable_cc) - (variable_dd * 10 + variable_bb) == 24:
                                                        list_willshoot.append(variable_aa)
                                                        list_willshoot.append(variable_cc)
                                                        list_willshoot.append(variable_symbol_minus)
                                                        list_willshoot.append(variable_dd)
                                                        list_willshoot.append(variable_bb)
                                                        variable_makeout = 3
                                                    else:
                                                        if (variable_aa * 10 + variable_dd) - (variable_bb * 10 + variable_cc) == 24:
                                                            list_willshoot.append(variable_aa)
                                                            list_willshoot.append(variable_dd)
                                                            list_willshoot.append(variable_symbol_minus)
                                                            list_willshoot.append(variable_bb)
                                                            list_willshoot.append(variable_cc)
                                                            variable_makeout = 3
                                                        else:
                                                            if (variable_aa * 10 + variable_dd) - (variable_cc * 10 + variable_bb) == 24:
                                                                list_willshoot.append(variable_aa)
                                                                list_willshoot.append(variable_dd)
                                                                list_willshoot.append(variable_symbol_minus)
                                                                list_willshoot.append(variable_cc)
                                                                list_willshoot.append(variable_bb)
                                                                variable_makeout = 3
                                                            else:
                                                                pass
def user_defined_atodby():
    global variable_V_average
    global variable_shotTime
    global variable_device_qn
    global variable_markerPosX
    global variable_theta
    global variable_markerPosY
    global variable_max
    global variable_Maker
    global variable_b
    global variable_mode
    global variable_c
    global variable_pidout
    global variable_pitchVal
    global variable_n
    global variable_markerSizeW
    global variable_MarkerSizeH
    global variable_i
    global variable_x
    global variable_X
    global variable_Y
    global variable_K
    global variable_v
    global variable_done
    global variable_hitting_num
    global variable_found
    global variable_done2
    global variable_UpperAngle
    global variable_LeftAngle
    global variable_sort_temp
    global variable_sorting_num
    global variable_sorting_index
    global variable_timer1
    global variable_aa
    global variable_bb
    global variable_cc
    global variable_dd
    global variable_tempp
    global variable_makeout
    global variable_symbol_plus
    global variable_symbol_minus
    global variable_symbol_multiple
    global variable_symbol_divide
    global list_LineList
    global list_MarkerList
    global list_k
    global list_m
    global list_MarkerList_2
    global list_sorted
    global list_willshoot
    global list_calc_num
    global list_temp_marker
    global pid_pid
    global pid_cpst
    global pid_speed
    global pid_pitch
    global pid_Follow_Line
    list_willshoot=RmList()
    if (variable_aa * 10 + variable_bb) * variable_cc == 24:
        list_willshoot.append(variable_aa)
        list_willshoot.append(variable_bb)
        list_willshoot.append(variable_symbol_multiple)
        list_willshoot.append(variable_cc)
        variable_makeout = 3
    else:
        if (variable_aa * 10 + variable_bb) * variable_dd == 24:
            list_willshoot.append(variable_aa)
            list_willshoot.append(variable_bb)
            list_willshoot.append(variable_symbol_multiple)
            list_willshoot.append(variable_dd)
            variable_makeout = 3
        else:
            if (variable_aa * 10 + variable_cc) * variable_bb == 24:
                list_willshoot.append(variable_aa)
                list_willshoot.append(variable_cc)
                list_willshoot.append(variable_symbol_multiple)
                list_willshoot.append(variable_bb)
                variable_makeout = 3
            else:
                if (variable_aa * 10 + variable_cc) * variable_dd == 24:
                    list_willshoot.append(variable_aa)
                    list_willshoot.append(variable_cc)
                    list_willshoot.append(variable_symbol_multiple)
                    list_willshoot.append(variable_dd)
                    variable_makeout = 3
                else:
                    if (variable_aa * 10 + variable_dd) * variable_bb == 24:
                        list_willshoot.append(variable_aa)
                        list_willshoot.append(variable_dd)
                        list_willshoot.append(variable_symbol_multiple)
                        list_willshoot.append(variable_bb)
                        variable_makeout = 3
                    else:
                        if (variable_aa * 10 + variable_dd) * variable_cc == 24:
                            list_willshoot.append(variable_aa)
                            list_willshoot.append(variable_dd)
                            list_willshoot.append(variable_symbol_multiple)
                            list_willshoot.append(variable_cc)
                            variable_makeout = 3
                        else:
                            pass
def start():
    global variable_V_average
    global variable_shotTime
    global variable_device_qn
    global variable_markerPosX
    global variable_theta
    global variable_markerPosY
    global variable_max
    global variable_Maker
    global variable_b
    global variable_mode
    global variable_c
    global variable_pidout
    global variable_pitchVal
    global variable_n
    global variable_markerSizeW
    global variable_MarkerSizeH
    global variable_i
    global variable_x
    global variable_X
    global variable_Y
    global variable_K
    global variable_v
    global variable_done
    global variable_hitting_num
    global variable_found
    global variable_done2
    global variable_UpperAngle
    global variable_LeftAngle
    global variable_sort_temp
    global variable_sorting_num
    global variable_sorting_index
    global variable_timer1
    global variable_aa
    global variable_bb
    global variable_cc
    global variable_dd
    global variable_tempp
    global variable_makeout
    global variable_symbol_plus
    global variable_symbol_minus
    global variable_symbol_multiple
    global variable_symbol_divide
    global list_LineList
    global list_MarkerList
    global list_k
    global list_m
    global list_MarkerList_2
    global list_sorted
    global list_willshoot
    global list_calc_num
    global list_temp_marker
    global pid_pid
    global pid_cpst
    global pid_speed
    global pid_pitch
    global pid_Follow_Line
    variable_symbol_plus = 50
    variable_symbol_minus = 51
    variable_symbol_multiple = 43
    variable_symbol_divide = 52
    gimbal_ctrl.set_rotate_speed(540)
    variable_UpperAngle = 15
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    chassis_ctrl.set_trans_speed(2)
    chassis_ctrl.set_rotate_speed(180)
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    gimbal_ctrl.angle_ctrl(0, variable_UpperAngle)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    vision_ctrl.marker_detection_color_set(rm_define.marker_detection_color_blue)
    vision_ctrl.set_marker_detection_distance(3)
    gun_ctrl.set_fire_count(1)
    time.sleep(1)
    user_defined_detect()
    for count in range(2):
        if vision_ctrl.get_env_brightness() > 0.3:
            media_ctrl.exposure_value_update(rm_define.exposure_value_small)
        else:
            if vision_ctrl.get_env_brightness() > 0.13:
                media_ctrl.exposure_value_update(rm_define.exposure_value_medium)
            else:
                media_ctrl.exposure_value_update(rm_define.exposure_value_large)
    gimbal_ctrl.yaw_ctrl(0)
    gimbal_ctrl.pitch_ctrl(variable_UpperAngle)
    list_MarkerList=RmList()
    while not variable_done2 == 1:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        if len(list_MarkerList) >= 16:
            if (15 in (list_MarkerList)) or (11 in (list_MarkerList)) or (13 in (list_MarkerList)) or (12 in (list_MarkerList)) or (14 in (list_MarkerList)) or (17 in (list_MarkerList)) or (18 in (list_MarkerList)) or (19 in (list_MarkerList)) or (16 in (list_MarkerList)):
                user_defined_detect()
            else:
                variable_done2 = 1
                time.sleep(2)
    time.sleep(1)