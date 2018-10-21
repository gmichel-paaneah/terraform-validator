from __future__ import absolute_import, division, print_function
import inspect
import sys
from builtins import (str)
from terraform_validator.custom_rules.BaseRule import BaseRule


def lineno():
    """Returns the current line number in our program."""
    return str(' - SnsTopicPolicyNotPrincipalRule - caller: ' + str(inspect.stack()[1][3]) + ' - line number: ' + str(
        inspect.currentframe().f_back.f_lineno))


class SnsTopicPolicyNotPrincipalRule(BaseRule):

    def __init__(self, cfn_model=None, debug=None):
        '''
        Initialize
        :param cfn_model:
        '''
        BaseRule.__init__(self, cfn_model, debug=debug)

    def rule_text(self):
        '''
        Get rule text
        :return:
        '''
        if self.debug:
            print('rule_text' + lineno())
        return 'SNS Topic policy should not allow Allow+NotPrincipal'

    def rule_type(self):
        '''
        Get rule type
        :return:
        '''
        self.type = 'VIOLATION::FAILING_VIOLATION'
        return 'VIOLATION::FAILING_VIOLATION'

    def rule_id(self):
        '''
        Get rule id
        :return:
        '''
        if self.debug:
            print('rule_id' + lineno())
        self.id = 'F8'
        return 'F8'

    def audit_impl(self):
        '''
        Audit
        :return: violations
        '''
        if self.debug:
            print('SnsTopicPolicyNotPrincipalRule - audit_impl' + lineno())

        violating_policies = []
        resources = self.cfn_model.resources_by_type('AWS::SNS::TopicPolicy')

        if len(resources) > 0:
            for resource in resources:
                if self.debug:
                    print('resource: ' + str(resource) + lineno())
                    print('vars: ' + str(vars(resource)) + lineno())

                if hasattr(resource, 'policy_document'):

                    if resource.policy_document:

                        if resource.policy_document.allows_not_principal():
                            violating_policies.append(str(resource.logical_resource_id))
                elif hasattr(resource, 'policy'):

                    if resource.policy_document:

                        if resource.policy.allows_not_principal():
                            violating_policies.append(str(resource.logical_resource_id))

        else:
            if self.debug:
                print('no violating_policies' + lineno())



        return violating_policies