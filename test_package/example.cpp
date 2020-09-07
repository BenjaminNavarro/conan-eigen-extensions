#include <Eigen/Dense>

int main() {
  auto res = Eigen::Matrix3d::Random().skew();
  auto res2 = Eigen::Quaterniond::Identity().integrate(Eigen::Vector3d::Ones());
}
