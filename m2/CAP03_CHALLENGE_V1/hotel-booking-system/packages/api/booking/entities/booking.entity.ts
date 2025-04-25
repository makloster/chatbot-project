import { Entity, Column, PrimaryGeneratedColumn, ManyToOne } from "typeorm";
import { User } from "../../users/entities/user.entity";
import { Room } from "../../inventory/entities/room.entity";

@Entity()
export class Booking {
  @PrimaryGeneratedColumn("uuid")
  id: string;

  @Column()
  checkIn: Date;

  @Column()
  checkOut: Date;

  @Column()
  status: string;

  @Column("decimal")
  totalAmount: number;

  @ManyToOne(() => User, (user) => user.bookings)
  user: User;

  @ManyToOne(() => Room, (room) => room.bookings)
  room: Room;
}
