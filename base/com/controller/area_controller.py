from flask import *

from base import app
from base.com.dao.area_dao import AreaDAO
from base.com.dao.city_dao import CityDAO
from base.com.dao.state_dao import StateDAO
from base.com.vo.area_vo import AreaVO
from base.com.vo.city_vo import CityVO


@app.route('/admin/load_area', methods=['get'])
def admin_load_area():
    try:
        state_dao = StateDAO()
        state_vo_list = state_dao.view_state()
        return render_template('admin/addArea.html', state_vo_list=state_vo_list)

    except Exception as ex:
        print('admin_load_area route exception occured>>>>>>>>>>', ex)


@app.route('/admin/ajax_area_city', methods=['get'])
def admin_ajax_area_city():
    try:
        city_dao = CityDAO()
        city_vo = CityVO()

        city_vo.city_state_id = request.args.get('state_id')
        city_vo_list = city_dao.view_ajax_area_city(city_vo)

        ajax_area_city = [i.as_dict() for i in city_vo_list]

        return jsonify(ajax_area_city)

    except Exception as ex:
        print('admin_ajax_area_city route exception occured>>>>>>>>>>', ex)


@app.route('/admin/insert_area', methods=['post'])
def admin_add_area():
    try:
        area_vo = AreaVO()
        area_dao = AreaDAO()

        area_vo.area_name = request.form.get('area_name')
        area_vo.area_pincode = request.form.get('area_pincode')
        area_vo.area_city_id = request.form.get('city_id')
        area_vo.area_state_id = request.form.get('state_id')

        area_dao.insert_area(area_vo)
        return redirect(url_for('admin_view_area'))

    except Exception as ex:
        print("admin_insert_area route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_area', methods=['get'])
def admin_view_area():
    try:
        area_dao = AreaDAO()
        area_vo_list = area_dao.view_area()
        return render_template('admin/viewarea.html', area_vo_list=area_vo_list)

    except Exception as ex:
        print("admin_view_area route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_area', methods=['get'])
def admin_delete_area():
    try:
        area_dao = AreaDAO()
        area_id = request.args.get('area_id')
        area_dao.delete_area(area_id)
        return redirect(url_for('admin_view_area'))
    except Exception as ex:
        print("in admin_delete_area route exception occured>>>>>>>>>>", ex)


@app.route('/admin/edit_area', methods=['get'])
def admin_edit_area():
    try:
        area_vo = AreaVO()
        area_dao = AreaDAO()
        state_dao = StateDAO()

        area_vo.area_id = request.args.get('area_id')
        area_vo_list = area_dao.edit_area(area_vo)
        state_vo_list = state_dao.view_state()
        print('state_vo_list>>>>>>', state_vo_list)
        return render_template('admin/editArea.html', state_vo_list=state_vo_list,
                               area_vo_list=area_vo_list)
    except Exception as ex:
        print("in admin_edit_area route exception occured>>>>>>>>>>", ex)


'''        
@app.route('/admin/update_area', methods=['POST'])
def admin_update_area():
    try:
        city_vo = CityVO()
        city_dao = CityDAO()

        city_vo.city_id = request.form.get('city_id')
        city_vo.city_name = request.form.get('city_name')
        city_vo.city_description = request.form.get('city_description')
        city_vo.city_state_id = request.form.get('city_state_id')
        city_dao.update_city(city_vo)
        return redirect(url_for('admin_view_area'))
    except Exception as ex:
        print("in admin_update_area route exception occured>>>>>>>>>>", ex)
'''