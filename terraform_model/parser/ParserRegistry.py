from __future__ import absolute_import, division, print_function
import inspect
from terraform_model.parser.SecurityGroupParser import SecurityGroupParser
from terraform_model.parser.Ec2NetworkInterfaceParser import Ec2NetworkInterfaceParser
from terraform_model.parser.Ec2InstanceParser import Ec2InstanceParser
from terraform_model.parser.LoadBalancerParser import LoadBalancerParser
from terraform_model.parser.LoadBalancerV2Parser import LoadBalancerV2Parser
from terraform_model.parser.IamGroupParser import IamGroupParser
from terraform_model.parser.IamUserParser import IamUserParser
from terraform_model.parser.IamRoleParser import IamRoleParser
from terraform_model.parser.SecurityGroupParser import SecurityGroupParser
from terraform_model.parser.WithPolicyDocumentParser import WithPolicyDocumentParser

def lineno():
    """Returns the current line number in our program."""
    return str(' -  ParserRegistry- line number: '+str(inspect.currentframe().f_back.f_lineno))


class ParserRegistry(object):
    """
    Parser registry
    """
    def __init__(self, debug=False):
        """
        Initialize
        :param debug: 
        """
        self.debug = debug

        if self.debug:
            print('ParserRegistry - init'+lineno())

        self.registry= {
            'AWS::EC2::SecurityGroup' : SecurityGroupParser,
            'AWS::EC2::NetworkInterface' : Ec2NetworkInterfaceParser,
            'AWS::EC2::Instance' : Ec2InstanceParser,
            'AWS::ElasticLoadBalancing::LoadBalancer' : LoadBalancerParser,
            'AWS::ElasticLoadBalancingV2::LoadBalancer' : LoadBalancerV2Parser,
            'AWS::IAM::Group' : IamGroupParser,
            'AWS::IAM::User' : IamUserParser,
            'AWS::IAM::Role' : IamRoleParser,
            'AWS::IAM::Policy' : WithPolicyDocumentParser,
            'AWS::IAM::ManagedPolicy' : WithPolicyDocumentParser,
            'AWS::S3::BucketPolicy' : WithPolicyDocumentParser,
            'AWS::SNS::TopicPolicy' : WithPolicyDocumentParser,
            'AWS::SQS::QueuePolicy' : WithPolicyDocumentParser
        }