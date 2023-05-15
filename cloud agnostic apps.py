# cloud agnostic apps means your app should be able to migrate to any cloud servce easily like aws, gcloud etc.
# and it should be able to use mulitple cloud services at once. like using aws  for data storage and azure machine for servers.

# 1. use Dependency injections:
# create a interface which define some set of services then implement it. so later if you want to use aws s3 instead of azure stor service
# we just need to write a new class for s3 funcnality and implement this interface. so by this way it's very easy for us to change services.

#2. use opensources services:
# open source services like cockroachdb for db and resdis for cahce, minio for bucket service, liquibse for db-migrations,
# because these services are provided my by most of the cloud providers,
# like azure, aws, etc. so by this technique we don't need to change our code again and again, if we switch cloud service.
# also if we don;t want to use cloude service to manage it, then we can manange it by our self, beause these are opensoure service.
# so using this thing we can easily switch to cloud and on-prem server without code change.

# 3. use automated pipelines for cicd. deployed via infrastructure as code declarative and repeatable automation. Argo-cd is tool for it.


# 4. use docker containers and kubernetes to orchestrate to these containers. becaue k8s is also open-source.and most of cloud providers support it.

# 5. use microservices architecture.

# 6. store logs of different microservices in single persisitance location.
# 7. scalable to multiple replicas without resource locking.
# 8. stateless services which can be terminate and migrated without consequences.


# note: we can use hashicorp terraform. it defines infrastrcuture as code. the hashicorp cli spins up the defined cloud infrastrcuture, on top of which dev deploy.
# in multi cloud approach we can write multiple hashicorp scripts. we can use ansible, chef and puppet as well for same

# mostly dev now use istio with k8s, for service mesh. it helps to easily automate application network. need to look into more in istio funcnality.

##################
### cloud-native container ###

# 1. every container should have single concern
# 2. provide health check API(readiness and live check)
# 3. Startup quickly and shutdown gracefully when terminated by SIGTERM and SIGKILL.
# 4. container images are immutable.
# 5. containers should be self-contained, with no dependencies on outside,
# except te config injection by runtime environment.
