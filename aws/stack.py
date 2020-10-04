from os import environ
from typing import cast

from aws_cdk.aws_route53 import HostedZone, ARecord, RecordTarget, IAliasRecordTarget
from aws_cdk.aws_route53_targets import BucketWebsiteTarget
from aws_cdk.aws_s3 import Bucket, CorsRule, HttpMethods, BucketAccessControl
from aws_cdk.core import Stack, Construct, App, RemovalPolicy, Duration, Environment


class MainStack(Stack):
    def __init__(self, scope: Construct, _id: str, **kwargs) -> None:
        super().__init__(scope, _id, **kwargs)
        domain_name = 'aaronmamparo.com'
        pip_hostname = 'pip.%s' % domain_name
        pip_repository_bucket = Bucket(
            self,
            'PipRepositoryBucket',
            bucket_name=pip_hostname,
            public_read_access=True,
            access_control=BucketAccessControl.PUBLIC_READ,
            website_index_document='index.html',
            removal_policy=RemovalPolicy.DESTROY,
            cors=[
                CorsRule(allowed_methods=[HttpMethods.GET], allowed_origins=['*']),
            ]
        )
        ARecord(
            self,
            'PipARecord',
            target=RecordTarget([], cast(IAliasRecordTarget, BucketWebsiteTarget(pip_repository_bucket))),
            zone=HostedZone.from_lookup(self, 'HostedZone', domain_name=domain_name),
            record_name=pip_hostname,
            ttl=Duration.seconds(60)
        )


if __name__ == '__main__':
    app = App()
    MainStack(app, 'pip-repository', env=Environment(
        account=environ.get('AWS_ACCOUNT_ID'),
        region=environ.get('AWS_DEFAULT_REGION')
    ))
    app.synth()
