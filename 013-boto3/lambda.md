# Lambda

Lambda is solving the problems of computer in the form of serverless. In the backend, again serverless is still on servers managed by cloudProvider.

1) Cost Optimization
2) Idenfity volumes that are created and not in used
3) Identify the VM's that are not started in last few weeks
4) Monitor and report the list of VM's that are used in the PROJECT.
5) Compliance : List the SG's that are having port open for all, nobody should use the EBS Volumes of type gp2, if there are any send an email ( sns ) to managment to migrate the data or delete that, s3 bucket with public access.
6) Everyday send the list of buckets that are created in last 24 hours and the authorization of it to make sure it's authentic.

7) VM created , volumes created to that and snapshosts were taken for that. VM+Volumes were deleted, but the underlying snaps are still there. This will be a potential billing.

# Cost Optimization

