# Generated by Django 3.2.25 on 2025-03-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_auto_20240418_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managementapiallowlistconfig',
            name='api',
            field=models.CharField(choices=[('grade_manager_list', '获取分级管理员列表'), ('grade_manager_create', '新建分级管理员'), ('grade_manager_update', '更新分级管理员'), ('grade_manager_member_list', '获取分级管理员成员列表'), ('grade_manager_member_add', '添加分级管理员成员'), ('grade_manager_member_delete', '删除分级管理员成员'), ('group_list', '获取用户组列表'), ('group_batch_create', '批量创建用户组'), ('group_update', '更新用户组'), ('group_delete', '删除用户组'), ('group_member_list', '获取用户组成员列表'), ('group_member_add', '添加用户组成员'), ('group_member_delete', '删除用户组成员'), ('group_policy_grant', '授权用户组'), ('group_policy_revoke', '回收用户组权限'), ('group_policy_delete', '删除用户组策略'), ('user_role_list', '获取用户加入的分级管理员列表'), ('user_role_group_list', '获取某个分级管理员下用户加入的用户组列表'), ('group_application_create', '创建用户组申请单'), ('v2_group_list', '[V2]用户组列表'), ('v2_group_batch_create', '[V2]批量创建用户组'), ('v2_group_update', '[V2]更新用户组'), ('v2_group_delete', '[V2]删除用户组'), ('v2_group_member_list', '[V2]获取用户组成员列表'), ('v2_group_member_add', '[V2]添加用户组成员'), ('v2_group_member_delete', '[V2]删除用户组成员'), ('v2_group_member_expired_at_update', '[V2]用户组成员续期'), ('v2_group_member_expired_at_batch_update', '[V2]用户组成员批量续期'), ('v2_group_subject_template_list', '[V2]获取用户组人员模板列表'), ('v2_group_policy_grant', '[V2]授权用户组'), ('v2_group_policy_revoke', '[V2]回收用户组权限'), ('v2_group_policy_delete', '[V2]删除用户组策略'), ('v2_group_policy_action_list', '[V2]用户组策略对应操作列表'), ('v2_group_application_create', '[V2]创建用户组申请单'), ('v2_group_application_renew', '[V2]用户组续期申请单'), ('v2_group_application_renew_batch', '[V2]用户组批量续期申请单'), ('v2_user_groups_belong_check', '[V2]判断用户与用户组归属'), ('v2_department_groups_belong_check', '[V2]判断部门与用户组归属'), ('v2_member_groups_detail_list', '[V2]用户组成员在组内的详情'), ('v2_grade_manager_detail', '[V2]分级管理员详情'), ('v2_grade_manager_create', '[V2]新建分级管理员'), ('v2_grade_manager_update', '[V2]更新分级管理员'), ('v2_grade_manager_application_create', '[V2]创建分级管理员创建申请单'), ('v2_grade_manager_application_update', '[V2]创建分级管理员更新申请单'), ('v2_subset_manager_create', '[V2]创建子集管理员'), ('v2_subset_manager_list', '[V2]子集管理员列表'), ('v2_application_approval', '[V2]申请单审批通知'), ('v2_application_cancel', '[V2]申请单取消')], help_text='*代表任意', max_length=64, verbose_name='API'),
        ),
    ]
