import QtQuick
import QtQuick3D

Node {
    id: rootNode
    property double robot_joint1: 400
    property double robot_joint2: 90
    property double robot_joint3: 90
    property int scale_x: 1
    property int scale_y: 1
    property int scale_z: 1
    Node {
        id: scene

        PerspectiveCamera {
            id: sceneCamera
            x: -709.052
            y: 849.243
            z: 1309.88684
            eulerRotation.x: -20
            eulerRotation.y: -25
        }

        Model {
            id: than_m1
            x: -58.266
            y: 3.067
            z: 0
            scale.x: scale_x
            scale.y: scale_y
            scale.z: scale_z
            source: "meshes/THAN_M1.mesh"
            eulerRotation.x: -90
            eulerRotation.y: 180
            materials: light_blue

            Model {
                id: canh_tay_1
                x: -0.331
                y: 207.785
                z: robot_joint1 //set
                scale.x: 1
                scale.y: 1
                scale.z: 1
                source: "meshes/CANH_TAY_1.mesh"
                eulerRotation.x: 180
                eulerRotation.y: 180
                eulerRotation.z: 360
                materials: green
                Model {
                    id: canh_tay_2
                    x: 1.495
                    y: 92.248
                    z: 8.31024
                    scale.x: 1
                    scale.y: 1
                    scale.z: 1
                    source: "meshes/CANH_TAY_2.mesh"
                    eulerRotation.x: 180
                    eulerRotation.y: 180
                    eulerRotation.z: robot_joint2 //set
                    materials: [blue]
                    Model {
                        id: canh_tay_3
                        x: 183.982
                        y: 2.627
                        z: -32.27737
                        scale.x: 1
                        scale.y: 1
                        scale.z: 1
                        source: "meshes/CANH_TAY_3.mesh"
                        eulerRotation.x: 0
                        eulerRotation.y: 0
                        eulerRotation.z: robot_joint3 //set
                        materials: yellow
                    }
                }
            }
        }

        DirectionalLight {
            id: lightDirectional
            x: -79.536
            y: 332.163
            brightness: 1
            z: -637.23572
            eulerRotation.x: 180
        }

        DirectionalLight {
            id: lightDirectional1
            x: 0
            y: 323.816
            z: 958.99146
            brightness: 0.5
        }
        DirectionalLight {
            id: directionalLight
            brightness: 0.5
            x: -809.143
            y: 311.361
            z: -0.00004
            eulerRotation.y: -90
        }

        DirectionalLight {
            id: directionalLight1
            x: 916.076
            y: 302.361
            brightness: 0.5
            eulerRotation.y: 90
            z: -9.00021
        }

        DirectionalLight {
            id: lightDirectional2
            x: -26.687
            y: 1056.216
            z: 0
            brightness: 0.5
            eulerRotation.x: -90
        }
    }
    Node {
        id: __materialLibrary__
        DefaultMaterial {
            id: light_blue
            objectName: "Default Material"
            diffuseColor: "#1bd1f6"
        }
        DefaultMaterial {
            id: green
            objectName: "Default Material"
            diffuseColor: "#00ff00"
        }
        DefaultMaterial {
            id: yellow
            objectName: "Default Material"
            diffuseColor: "#f3ff00"
        }
        DefaultMaterial {
            id: blue
            objectName: "Default Material"
            diffuseColor: "#6593f4"
        }
    }
}
