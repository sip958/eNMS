script_properties = (
    'name',
    'type',
    'description',
    'waiting_time',
)

netmiko_config_properties = script_properties + (
    'vendor',
    'operating_system',
    'content',
    'driver',
    'global_delay_factor',
    'netmiko_type'
)

napalm_config_properties = script_properties + (
    'vendor',
    'operating_system',
    'content',
)

file_transfer_properties = script_properties + (
    'vendor',
    'operating_system',
    'source_file',
    'destination_file',
    'file_system',
    'direction'
)

netmiko_validation_properties = script_properties + (
    'vendor',
    'operating_system',
    'command1',
    'command2',
    'command3',
    'pattern1',
    'pattern2',
    'pattern3'
)

napalm_getters_properties = script_properties + (
    'getters',
)

ansible_playbook_properties = script_properties + (
    'vendor',
    'operating_system',
    'playbook_path',
)

type_to_properties = {
    'netmiko_config': netmiko_config_properties,
    'napalm_config': napalm_config_properties,
    'file_transfer': file_transfer_properties,
    'netmiko_validation': netmiko_validation_properties,
    'napalm_getters': napalm_getters_properties,
    'ansible_playbook': ansible_playbook_properties
}
